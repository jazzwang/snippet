# Joplin

- Git Repo
  - https://github.com/laurent22/joplin
- Website
  - https://joplinapp.org/

## 2026-06-06

- 緣起：
  - 2018~2024 這段期間，為了做個人知識管理 (PKM) 又要兼顧隱私，所以從 Dropbox Paper 移到了 Joplin
  - Joplin 的 Web Clipper 也很好用 https://joplinapp.org/help/apps/clipper/
  - 今天看了 https://rar.design/posts/obsidian-ai-second-brain-2026 確實想起前陣子很熱門的 LLM Wiki
  - 看到諸多關於 Obsidian CLI 與 MCP 的討論跟實作，想想或許可以把以前 Joplin 的資料移轉到 Obsidian
  - 看來還要研究一下 Obsidian Web Clipper - https://obsidian.md/clipper
- 研究：
  - Google Search
    - https://github.com/hugobatista/joplin-to-obsidian
    - https://forum.obsidian.md/t/importing-from-joplin/41483
  - AI Mode
<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
joplin to obsidian
</td></tr><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search AI Mode
</td></tr><tr><td>A:</td><td>

Migrating your notes from Joplin to Obsidian is a straightforward process. Because Joplin natively supports exporting to plain text, you can move your data over without losing your organizational structure. [1, 2] 
## How to Migrate in 3 Steps

   1. Export from Joplin
   * Open the [Joplin desktop application](https://joplinapp.org/).
      * Click on File > Export all in the top menu.
      * Select MD - Markdown + Front Matter as the format. This ensures that note metadata like tags, creation dates, and original timestamps are embedded directly inside the files.
      * Choose a target folder on your computer to save the export. [1, 2, 3, 4, 5, 6] 
   2. Move to Obsidian
   * Create a new folder on your computer to act as your destination.
      * Copy or move all the exported Markdown files and folders from the previous step into this new folder.
      * Open the Obsidian application.
      * Click Open folder as vault and select your newly filled directory. [1, 3, 6, 7, 8] 
   3. Format Attachments (If Needed)
   * Joplin exports all non-markdown attachments into a global folder called _resources.
      * In Obsidian, open your settings and choose Files and links.
      * Change your attachment folder settings to match where your images/PDFs are stored so links display properly in preview mode. [1, 3, 9, 10, 11] 
   
------------------------------
## Comparison: Key Workflow Differences
If you are evaluating which tool to stick with long-term, their design philosophies cater to very different workflows: [12] 

| Feature [13, 14, 15, 16, 17, 18, 19, 20] | Joplin | Obsidian |
|---|---|---|
| Organization | Traditional, rigid notebook/sub-notebook structure. | Networked system built on dynamic bidirectional linking and tags. |
| Data Storage | Managed inside a local SQLite database. | Direct, transparent storage as native .md files in local folders. |
| Visual Mapping | Standard folder hierarchies and list views. | Interactive Graph View and a native visual whiteboard canvas. |
| Ecosystem | A smaller selection of roughly 200 essential plugins. | Massive library of over 900 custom community plugins. |
| Syncing | Free synchronization through personal cloud storage accounts (Dropbox, WebDAV). | Seamless cloud sync via a paid official subscription or manual workarounds. |

## Summary Checklist for Choosing

* Choose Joplin if you want an open-source, Evernote-style folder system that offers free cross-device cloud syncing right out of the box. [13, 14, 20] 
* Choose [Obsidian](https://obsidian.md/) if you prefer a "second brain" workflow, highly customizable themes, extensive plugin options, and interconnected, linked ideas. [14, 19, 20] 

------------------------------
To ensure a smooth transition, would you like to explore community plugins to handle broken internal links, or do you need assistance setting up a free cross-device syncing workaround for your new vault? [2, 17, 21] 

[1] [https://forum.obsidian.md](https://forum.obsidian.md/t/importing-from-joplin/41483)
[2] [https://petronellatech.com](https://petronellatech.com/blog/obsidian-vs-joplin/)
[3] [https://github.com](https://github.com/0x6f677548/joplin-to-obsidian)
[4] [https://nelsonslog.wordpress.com](https://nelsonslog.wordpress.com/2023/03/29/migrating-joplin-to-obsidian-metadata/)
[5] [https://forum.obsidian.md](https://forum.obsidian.md/t/an-automation-tool-for-helping-people-migrate-from-joplin-to-obsidian/21700)
[6] [https://github.com](https://github.com/luxi78/joplin2obsidian)
[7] [https://forum.obsidian.md](https://forum.obsidian.md/t/import-notes-from-joplin/15676)
[8] [https://github.com](https://github.com/anpigon/obsidian-joplin-plugin)
[9] [https://www.reddit.com](https://www.reddit.com/r/ObsidianMD/comments/1mc3wr0/switching_from_joplin_to_obsidian/)
[10] [https://joplinapp.org](https://joplinapp.org/help/)
[11] [https://addozhang.medium.com](https://addozhang.medium.com/obsidian-plugin-image-upload-toolkit-came-to-1-0-7921c68ef22f)
[12] [https://viazure.cc](https://viazure.cc/posts/tinkering/migrating-from-joplin-to-obsidian/)
[13] [https://medium.com](https://medium.com/@juliamalinina_55009/how-i-replaced-obsidian-with-joplin-9a2b9c44dd0a)
[14] [https://www.youtube.com](https://www.youtube.com/watch?v=XPbxhq4w9Sw)
[15] [https://discourse.joplinapp.org](https://discourse.joplinapp.org/t/convert-obsidian-vault-to-joplin/37475)
[16] [https://www.reddit.com](https://www.reddit.com/r/joplinapp/comments/u4bwa3/moving_from_obsidian_to_joplin/)
[17] [https://www.reddit.com](https://www.reddit.com/r/joplinapp/comments/17f5ss5/moving_to_obsidian/)
[18] [https://www.reddit.com](https://www.reddit.com/r/joplinapp/comments/1k6l6fc/joplin_vs_obsidian_why_joplin_is_a_winner/)
[19] [https://www.youtube.com](https://www.youtube.com/watch?v=AybHmYmVd7g)
[20] [https://www.youtube.com](https://www.youtube.com/watch?v=WN6_bXyc7_w)
[21] [https://www.reddit.com](https://www.reddit.com/r/ObsidianMD/comments/ybaygx/should_i_switch_from_joplin_to_obsidian/)

</td></tr>
</table>
