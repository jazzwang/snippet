(function() {
    /**
     * Converts a DOM node into Markdown syntax.
     * @param {Node} node The DOM node to convert.
     * @param {Object} options Configuration options for the conversion.
     * @param {number} options.listDepth Current nesting level for lists, used for indentation.
     * @param {Function} options.linkTransform Function to customize link markdown.
     * @param {Function} options.imgTransform Function to customize image markdown.
     * @param {Function} options.codeTransform Function to customize inline code markdown.
     * @param {Function} options.blockquoteTransform Function to customize blockquote markdown.
     * @returns {string} The Markdown representation of the node.
     */
    function domToMarkdownInternal(node, options = {}) {
        let markdown = '';
        const defaultOptions = {
            listDepth: 0,
            linkTransform: (href, text) => `[${text}](${href})`,
            imgTransform: (src, alt) => `![${alt}](${src})`,
            codeTransform: (code) => `\`${code}\``,
            blockquoteTransform: (text) => `> ${text.split('\n').join('\n> ')}`,
        };
        options = { ...defaultOptions, ...options };

        // Helper to recursively process children and concatenate their markdown
        function processChildren(parentNode) {
            let childrenMarkdown = '';
            for (const child of parentNode.childNodes) {
                childrenMarkdown += domToMarkdownInternal(child, options);
            }
            return childrenMarkdown;
        }

        switch (node.nodeType) {
            case Node.TEXT_NODE:
                // Normalize whitespace: replace multiple spaces with one, trim leading/trailing.
                let text = node.textContent.replace(/\s+/g, ' ').trim();
                if (text.length > 0) {
                    markdown += text;
                }
                break;

            case Node.ELEMENT_NODE:
                const tagName = node.tagName.toLowerCase();

                // Tags to ignore completely (and their children)
                const ignoredTags = ['script', 'style', 'meta', 'link', 'noscript', 'canvas', 'svg', 'iframe', 'form', 'input', 'button', 'select', 'textarea', 'label', 'head'];
                if (ignoredTags.includes(tagName)) {
                    break;
                }

                const childrenContent = processChildren(node);

                switch (tagName) {
                    case 'h1':
                    case 'h2':
                    case 'h3':
                    case 'h4':
                    case 'h5':
                    case 'h6':
                        const headingLevel = parseInt(tagName.charAt(1));
                        markdown += `\n\n${'#'.repeat(headingLevel)} ${childrenContent.trim()}\n\n`;
                        break;
                    case 'p':
                        markdown += `\n\n${childrenContent.trim()}\n\n`;
                        break;
                    case 'a':
                        const href = node.getAttribute('href');
                        const linkText = childrenContent.trim() || href;
                        if (href && linkText) {
                            markdown += options.linkTransform(href, linkText);
                        } else {
                            markdown += linkText;
                        }
                        break;
                    case 'strong':
                    case 'b':
                        markdown += `**${childrenContent.trim()}**`;
                        break;
                    case 'em':
                    case 'i':
                        markdown += `*${childrenContent.trim()}*`;
                        break;
                    case 'code':
                        // Only for inline <code>. If parent is <pre>, it's handled by 'pre'.
                        if (node.parentNode.tagName.toLowerCase() !== 'pre') {
                            markdown += options.codeTransform(childrenContent.trim());
                        } else {
                            markdown += childrenContent; // Handled as part of pre's textContent
                        }
                        break;
                    case 'pre':
                        const codeBlockContent = node.textContent; // Preserve original whitespace for pre
                        if (codeBlockContent.trim().length > 0) {
                            markdown += `\n\n\`\`\`\n${codeBlockContent.trim()}\n\`\`\`\n\n`;
                        }
                        break;
                    case 'img':
                        const src = node.getAttribute('src');
                        const alt = node.getAttribute('alt') || '';
                        if (src) {
                            markdown += options.imgTransform(src, alt);
                        }
                        break;
                    case 'ul':
                    case 'ol':
                        const listItems = Array.from(node.children).filter(child => child.tagName.toLowerCase() === 'li');
                        if (listItems.length === 0) break;

                        let listMarkdown = '';
                        const indentSpaces = options.listDepth * 2; // 2 spaces per nesting level for indentation

                        listItems.forEach((li, index) => {
                            const bullet = tagName === 'ul' ? '- ' : `${index + 1}. `;
                            // Recursively convert list item content with increased depth
                            const liContent = domToMarkdownInternal(li, { ...options, listDepth: options.listDepth + 1 }).trim();

                            // Indent subsequent lines of a multi-line list item
                            const indentedLiContent = liContent.split('\n').map((line, i) =>
                                i === 0 ? line : ' '.repeat(indentSpaces + bullet.length) + line
                            ).join('\n');
                            listMarkdown += `${' '.repeat(indentSpaces)}${bullet}${indentedLiContent}\n`;
                        });
                        markdown += `\n${listMarkdown}\n`; // Add extra newlines for block separation
                        break;
                    case 'li':
                        // li content is processed by its parent ul/ol
                        markdown += childrenContent;
                        break;
                    case 'blockquote':
                        const blockquoteContent = childrenContent.trim();
                        if (blockquoteContent) {
                            markdown += `\n\n${options.blockquoteTransform(blockquoteContent)}\n\n`;
                        }
                        break;
                    case 'hr':
                        markdown += `\n\n---\n\n`;
                        break;
                    case 'br':
                        markdown += `  \n`; // Markdown line break
                        break;
                    case 'table':
                        let tableMarkdown = '';
                        let headerCells = [];
                        let bodyDataRows = []; // Stores array of arrays of cell markdown

                        // 1. Check for header in <thead>
                        const theadRow = node.querySelector(':scope > thead > tr');
                        if (theadRow) {
                            headerCells = Array.from(theadRow.children)
                                                .map(cell => domToMarkdownInternal(cell, { ...options }).trim());
                        }

                        // 2. Process <tbody> rows
                        const tbodyRows = Array.from(node.querySelectorAll(':scope > tbody > tr'));
                        tbodyRows.forEach(row => {
                            bodyDataRows.push(Array.from(row.children)
                                                    .map(cell => domToMarkdownInternal(cell, { ...options }).trim()));
                        });

                        // 3. Process direct <table> > <tr> (for simple tables without thead/tbody)
                        // This only runs if no thead/tbody content was found yet.
                        if (headerCells.length === 0 && bodyDataRows.length === 0) {
                            const directRows = Array.from(node.querySelectorAll(':scope > tr'));
                            directRows.forEach((row, index) => {
                                const cells = Array.from(row.children)
                                                      .map(cell => domToMarkdownInternal(cell, { ...options }).trim());
                                // Heuristic: if it's the first row and all cells are <th>, treat as header
                                if (index === 0 && cells.length > 0 && Array.from(row.children).every(c => c.tagName.toLowerCase() === 'th')) {
                                    headerCells = cells;
                                } else {
                                    bodyDataRows.push(cells);
                                }
                            });
                        } else if (headerCells.length === 0 && bodyDataRows.length > 0) {
                            // Heuristic: if no explicit thead but tbody rows exist, and the first tbody row is all th,
                            // treat it as the header and remove it from body rows.
                            if (bodyDataRows[0].length > 0 && Array.from(tbodyRows[0].children).every(c => c.tagName.toLowerCase() === 'th')) {
                                headerCells = bodyDataRows.shift();
                            }
                        }

                        // Determine the maximum number of columns, either from header or body rows
                        let columnCount = headerCells.length;
                        if (columnCount === 0 && bodyDataRows.length > 0) {
                            columnCount = Math.max(...bodyDataRows.map(row => row.length));
                        }
                        if (columnCount === 0 && headerCells.length === 0) break; // No discernible table content

                        // If no header, but we have body rows, create a dummy header row of empty strings
                        if (headerCells.length === 0 && bodyDataRows.length > 0) {
                             headerCells = Array(columnCount).fill('');
                        }

                        // Render the Markdown table
                        tableMarkdown += `\n\n`;
                        tableMarkdown += `| ${headerCells.map(h => h || '').join(' | ')} |\n`;
                        tableMarkdown += `|${Array(columnCount).fill('---').join('|')}|\n`;

                        bodyDataRows.forEach(row => {
                            // Pad row cells to match columnCount, fill with empty strings
                            const paddedRow = row.slice(0, columnCount).concat(Array(Math.max(0, columnCount - row.length)).fill(''));
                            tableMarkdown += `| ${paddedRow.map(c => c || '').join(' | ')} |\n`;
                        });
                        markdown += tableMarkdown;
                        markdown += `\n\n`;
                        break;

                    case 'div':
                    case 'span':
                    case 'section':
                    case 'article':
                    case 'main':
                    case 'header':
                    case 'footer':
                    case 'nav':
                    case 'aside':
                        // Generic containers, just process children's content
                        markdown += childrenContent;
                        break;

                    default:
                        // For other elements not explicitly handled, just pass through their children's content
                        markdown += childrenContent;
                        break;
                }
                break;
            default:
                // Ignore comments, processing instructions, etc.
                break;
        }
        return markdown;
    }

    /**
     * Converts a given DOM node (or document.body by default) into a clean Markdown string.
     * This function is exposed globally for easy use in the DevTools console.
     * @param {Node} [rootNode=document.body] The root DOM node to start conversion from.
     * @param {Object} [options={}] Optional configuration for the conversion.
     * @returns {string} The final Markdown string.
     */
    window.domToMarkdown = function(rootNode = document.body, options = {}) {
        let result = domToMarkdownInternal(rootNode, options);
        // Clean up leading/trailing newlines and collapse multiple newlines
        result = result.replace(/^\n+/, '').replace(/\n+$/, ''); // Trim leading/trailing
        result = result.replace(/(\n\n\n+)/g, '\n\n'); // Collapse more than two newlines to two
        return result;
    };

    // Automatically convert and download the Markdown of the current document.body
    // when this script is pasted into the console.
    const markdownContent = window.domToMarkdown(document.body);
    const title = document.title && document.title.length > 0 ? document.title.replace(/[^\w\s-]/g, '').replace(/[\s_-]+/g, '_').trim() : 'untitled';
    const filename = `${title}.md`;

    const blob = new Blob([markdownContent], { type: 'text/markdown' });
    const url = URL.createObjectURL(blob);

    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
})();
