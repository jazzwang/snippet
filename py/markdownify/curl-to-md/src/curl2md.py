import requests
import argparse
from markdownify import markdownify as md
import sys

def fetch_and_convert(url, output_file):
    """
    Fetches the content from a URL with a custom User-Agent,
    converts the HTML to Markdown, and saves it to a file.
    """
    # 1. Define the User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
    }

    try:
        # 2. Fetch the content from the URL
        print(f"Fetching content from: {url}")
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        html_content = response.text

        # 3. Convert HTML to Markdown
        print("Converting HTML to Markdown...")
        markdown_content = md(html_content, heading_style="ATX") # ATX style uses #'s for headings (e.g., # Header 1)

        # 4. Save the Markdown to the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        print(f"✅ Success! Content saved to: {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error during request: {e}", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"❌ Error writing to file: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """
    Main function to parse arguments and call the fetch/convert function.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Fetch HTML from a URL, convert it to Markdown, and save it to a file."
    )
    
    # Required positional argument for the URL
    parser.add_argument(
        'url',
        type=str,
        help="The URL of the webpage to fetch."
    )
    
    # Required optional argument for the output file
    parser.add_argument(
        '-o', '--output',
        type=str,
        required=True,
        dest='output_file',
        help="The path to the output Markdown file (e.g., output.md)."
    )

    args = parser.parse_args()

    # Call the core function with the parsed arguments
    fetch_and_convert(args.url, args.output_file)

if __name__ == '__main__':
    main()