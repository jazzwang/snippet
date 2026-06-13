# ARM Metis

- Git Repo
  - https://github.com/arm/metis

> Metis is an open-source, AI-driven tool for deep security code review

----

##  Agentic AI-powered Arm Metis advances security vulnerability discovery in software

> 由人工智慧驅動的 Arm Metis 技術，提升了軟體中安全漏洞的檢測能力。

- Source: https://newsroom.arm.com/blog/arm-metis-agentic-ai-security

> The open-sourced agentic AI security framework, delivers contextual AI-powered security analysis at scale to detect software vulnerabilities earlier and save time and costs

> 這個開源的代理式 AI 安全架構，能夠以大規模的方式，運用 AI 技術進行安全分析。如此一來，就能更早地發現軟體中的漏洞，從而節省時間和成本。

By [Mark Hambleton](https://newsroom.arm.com/author/mark-hambleton), SVP, Software, Arm
作者：Arm 公司軟體事業部高級副總裁 Mark Hambleton

In the era of AI, modern software systems are built across increasingly complex codebases, frameworks, runtimes and libraries. As these systems scale, so does the challenge of identifying security vulnerabilities before products reach customers.

> 在人工智慧時代，現代的軟體系統是建立在越來越複雜的程式碼、架構、執行環境和函式庫之上的。隨著這些系統規模的不斷擴大，要在產品到達客戶手中之前找出其中的安全漏洞，也變得越來越困難。

To help address this challenge, [Arm’s product security team has developed and open-sourced **Metis**](https://github.com/arm/metis), an agentic AI security framework designed to identify complex security issues across large-scale codebases. Within Arm, Metis is already running across more than 130 software projects, with plans for Arm-wide software adoption by late 2026.

> 為了應對這個挑戰，Arm 的產品安全團隊開發了 Metis 這個人工智能安全框架，並將其開源。Metis 專門用於識別大型代碼庫中的各種複雜安全問題。在 Arm 內部，Metis 已經被應用於 130 多個軟體專案中，並計劃在 2026 年底之前在 Arm 的所有軟體中全面推廣。

Metis is an important step forward in how the industry can approach software security verification, helping engineering teams identify issues earlier, reduce development overhead and improve the overall security and performance of products.

> Metis 是該領域在軟體安全驗證方面的重大進步。它能幫助工程團隊更早地發現問題、降低開發成本，進而提升產品的整體安全性和性能。

### Detecting complex vulnerabilities earlier and at greater scale
> 更早、更大範圍地偵測各種複雜的漏洞

Traditional static analysis tools are often limited in their ability to identify vulnerabilities that span multiple components, systems or layers of software. By combining advanced analysis techniques with AI-enabled workflows, [Metis identifies more sophisticated security vulnerabilities](https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/empowering-engineers-with-ai-enabled-security-code-review) that are difficult to detect using existing approaches, as well as identifying them earlier in the process. This helps save time and reduce costs on engineering resources and validation cycles, while improving product quality.

> 傳統的靜態分析工具在識別那些涉及多個組件、系統或軟體層面的安全漏洞時，往往存在侷限性。透過將先進的分析技術與人工智能技術相結合，Metis 能夠發現那些使用傳統方法很難偵測到的複雜安全漏洞，並且能夠更早地發現這些漏洞。這不僅有助於節省時間和成本，降低工程開發及驗證的費用，同時也能提升產品品質。

Metis is improving detection quality and developer productivity, with internal Arm benchmarks that have not been trained by AI showing that it delivers:

> Metis 在提升檢測準確度與開發人員的效率方面表現出色。根據未經 AI 訓練的 Arm 內部測試結果顯示，Metis 確實能夠達到預期效果。

* Up to **10x higher true positive rates**; and
  > 真正的正確率可高出 10 倍；此外……
* Approximately **50% fewer false positives** compared to leading static analysis tools.
  > 與領先的靜態分析工具相比，誤報率約低 50%。

False positives consume valuable engineering time and can reduce trust in automated tooling. By reducing false positives, Metis helps engineering teams focus on the issues that matter most, accelerating remediation and reducing wasted effort during validation and review.

> 誤報會浪費寶貴的工程開發時間，並可能降低人們對自動化工具的信任度。透過減少誤報，Metis 能幫助工程團隊專注於最需要解決的問題，從而加快問題的解決速度，並避免在驗證和審查過程中不必要的浪費。

### How Metis works for contextual security analysis

> Metis 如何用於情境式安全分析

<mark>Metis is built on a **retrieval-augmented generation (RAG)** architecture</mark> that combines large language models (LLMs) with project-specific knowledge to deliver contextual security analysis. Unlike traditional static analysis tools that rely primarily on fixed rules and pattern matching, Metis understands code in context and creates a custom knowledge base using source code, build files and documentation, giving a deeper understanding of how systems are designed and intended to operate. This allows Metis to analyze entire repositories, individual files, pull requests or recent code changes, so it can identify more complex vulnerabilities across functions, components and workflows.

> Metis 採用的是一種稱為「檢索增強型生成」（RAG）的架構。該架構將大型語言模型與特定於某個專案的知識相結合，從而實現更精確的安全性分析。與那些主要依賴固定規則和模式匹配的傳統靜態分析工具不同，Metis 能夠在具體的上下文中理解代碼。它還能夠利用原始碼、建構檔案和說明文件來建立專用的知識庫，進而更深入地瞭解系統的設計和運作方式。這使得 Metis 能夠分析整個代碼庫、單個檔案、 Pull Request 或最近的代碼變更，從而更有效地找出各個功能、組件和工作流程中的各種漏洞。

In addition, Metis can validate findings from both its own analysis and external static application security testing (SAST) tools. By navigating source code, constructing detailed graphs, gathering supporting evidence and reasoning over potential security issues, Metis can distinguish likely vulnerabilities from false positives.

> 此外，Metis 還能夠驗證其自身分析所得的結果，以及外部靜態應用程式安全測試工具所檢出的結果。透過分析原始碼、建立詳細的圖表、收集相關證據，並對各種潛在的安全問題進行推理，Metis 能夠區分出真正的漏洞和誤報。

  
  ![](https://newsroom.arm.com/wp-content/uploads/2026/05/Metis-Newsroom-blog_drk.png)

  *Arm’s internal benchmark showing Metis with GPT-5.5-Cyber model through OpenAI Daybreak*

  > Arm 的內部測試結果顯示，Metis 在與 OpenAI 的 Daybreak 平臺上，使用 GPT-5.5-Cyber 模型時的表現如何。

In Arm’s internal deployments, Metis uses OpenAI’s GPT-5.5-Cyber through OpenAI Daybreak as a part of its defensive security workflow and pairs advanced AI reasoning with deep, respository-specific context across source code. 

> 在 Arm 的內部應用中，Metis 透過 OpenAI Daybreak 來使用 OpenAI 的 GPT-5.5-Cyber。這套技術被用於 Arm 的防禦性安全工作流程中。Metis 將先進的 AI 推理能力，與源代碼中的各種上下文資訊相結合。
 
Metis also explains why a particular issue matters, providing developers and engineers with clear, actionable summaries that help accelerate remediation and improve secure development practices. Metis supports a wide range of programming languages, including C, C++, Python and Rust to name a few, with a full list of supported languages available [here](https://github.com/arm/metis#supported-languages). 

> Metis 還解釋了為何某個問題如此重要，它為開發人員和工程師提供簡明扼要的說明，從而幫助他們更快地解決問題，並提升安全開發的效率。Metis 支援多種程式設計語言，包括 C、C++、Python 和 Rust 等。支援的語言清單可在此處查看。
 
### Open collaboration for a more secure ecosystem

> 開放式合作，打造更安全的生態系統

Security challenges are industry-wide challenges. This is why Arm chose to open source Metis and make it available to the broader ecosystem. The project is already seeing adoption beyond Arm, including interest from partners exploring how AI-enabled vulnerability discovery can improve their own development workflows.

> 安全挑戰是整個產業都面臨的問題。正因如此，Arm 決定將 Metis 開源，讓更廣泛的生態系統能夠使用它。目前，已有不少非 Arm 旗下的團體開始使用這個項目，其中包括一些希望瞭解如何運用人工智能來發現漏洞、從而改善自身開發流程的合作伙伴。
 
While Metis is initially focusing on software vulnerability discovery, Arm is already expanding the technology into new domains. The project recently added support for Verilog and Arm is working with ecosystem partners to explore how Metis can help support more automated approaches to hardware vulnerability verification.

> 雖然 Metis 目前主要致力於軟體漏洞的檢測，但 Arm 已經開始將這項技術應用於其他領域。該項目最近新增了對 Verilog 語言的支援，Arm 正與生態系統中的合作夥伴共同探索，如何利用 Metis 來提升硬件漏洞檢測的自動化程度。
 
As AI systems, silicon and software stacks become increasingly interconnected, security analysis needs to evolve beyond isolated software scanning toward broader system-level verification. 

> 隨著人工智慧系統的發展，矽晶片與各種軟體之間的連結也越來越緊密。因此，安全性分析的方式也必須從單純的軟體掃描，轉變為更全面的系統級驗證。

![](https://newsroom.arm.com/wp-content/uploads/2026/05/Screenshot-2026-05-28-at-13.18.03.png)

### Building the future of AI-enabled vulnerability discovery

> 打造由人工智慧驅動的漏洞發現技術的未來

AI is reshaping how security teams identify and address vulnerabilities. With Metis, Arm is helping pioneer a new generation of AI-enabled security tooling designed for the scale and complexity of modern software, helping developers and engineers address vulnerabilities faster while reducing validation cost and engineering effort.

> AI 正在改變安全團隊識別和處理漏洞的方式。透過 Metis，Arm 正助力打造新一代的 AI 驅動型安全工具。這些工具專為應對現代軟體的複雜性而設計，能幫助開發人員和工程師更快地找出漏洞，同時降低驗證成本和工程開發的工作量。
 
By improving vulnerability discovery, reducing developer overhead and expanding verification across software, Metis helps strengthen the foundation for the next generation of secure computing.

> 透過提升漏洞發現的能力、減少開發人員的負擔，並擴大對軟體各部分的驗證範圍，Metis 有助於為下一代安全計算奠定更堅實的基礎。

Learn more about Metis and explore the [open-source project on GitHub](https://github.com/arm/metis) or contact the Arm Product security team on [metis@arm.com](mailto:metispsirt@arm.com)

> 進一步瞭解 Metis 的相關資訊，可參考 GitHub 上的開源專案，或透過 metis@arm.com 與 Arm 產品安全團隊聯絡。