# Github Page

## 2025-01-08

- ( 2025-01-08 21:29:57 )
- 紀錄一下 Github Page 是否支援動態網站託管
- 參考：https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages

### About GitHub Pages

GitHub Pages is a <mark>static site hosting service</mark> that takes HTML, CSS, and JavaScript files straight from a repository on GitHub, optionally runs the files through a build process, and publishes a website. You can see examples of GitHub Pages sites in the GitHub Pages examples collection.

> [!NOTE]
> GitHub Pages 是一種<mark>靜態網站託管服務</mark>，它直接從 GitHub 上的儲存庫取得 HTML、CSS 和 JavaScript 文件，可以選擇透過建置流程執行文件，然後發佈網站。您可以在 GitHub Pages 範例集合中查看 GitHub Pages 網站的範例。

GitHub Pages now uses <mark>GitHub Actions</mark> to execute the <mark>Jekyll build</mark>. When using a branch as the source of your build, GitHub Actions must be enabled in your repository if you want to use the built-in Jekyll workflow. Alternatively, if GitHub Actions is unavailable or disabled, adding a `.nojekyll` file to the root of your source branch will bypass the Jekyll build process and deploy the content directly. For more information on enabling GitHub Actions, see [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository).

> [!NOTE]
> GitHub Pages 現在使用 <mark>GitHub Actions</mark> 來執行 <mark>Jekyll 建置</mark>。當使用分支作為建置來源時，如果您想使用內建 Jekyll 工作流程，則必須在儲存庫中啟用 GitHub Actions。或者，如果 GitHub Actions 不可用或被停用，則將 `.nojekyll` 檔案新增至來源分支的根目錄將繞過 Jekyll 建置流程並直接部署內容。有關啟用 GitHub Actions 的更多信息，請參閱[管理儲存庫的 GitHub Actions 設定](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository)。

### Prohibited uses  禁止用途

GitHub Pages is not intended for or allowed to be used as a free web-hosting service to run your online business, e-commerce site, or any other website that is primarily directed at either facilitating commercial transactions or providing commercial software as a service (SaaS). GitHub Pages sites shouldn't be used for sensitive transactions like sending passwords or credit card numbers.

> [!NOTE]
> GitHub Pages 無意或**不允許用作**免費網站寄存服務來經營您的線上業務、電子商務網站或**任何其他主要旨在促進商業交易或提供商業軟體即服務的其他網站（軟體即服務）**。 GitHub Pages 網站不應用於發送密碼或信用卡號等敏感交易。

In addition, your use of GitHub Pages is subject to the GitHub Terms of Service, including the restrictions on get-rich-quick schemes, sexually obscene content, and violent or threatening content or activity.

> [!NOTE]
> 此外，您對 GitHub Pages 的使用須遵守 GitHub 服務條款，包括快速致富計畫、色情內容以及暴力或威脅內容或活動的限制。

### Usage limits  使用限制

GitHub Pages sites are subject to the following usage limits:

> GitHub Pages 網站受到以下使用限制：

GitHub Pages source repositories have a recommended limit of 1 GB. For more information, see About large files on GitHub.

> GitHub Pages 來源儲存庫的建議限制為 1 GB。有關更多信息，請參閱 GitHub 上的關於大文件。

Published GitHub Pages sites may be no larger than 1 GB.

> 已發布的 GitHub Pages <mark>網站不得大於 1 GB</mark>。

GitHub Pages deployments will timeout if they take longer than 10 minutes.

> 如果 GitHub Pages <mark>部署時間超過 10 分鐘，則會逾時</mark>。

GitHub Pages sites have a soft bandwidth limit of 100 GB per month.

> GitHub Pages 網站的軟<mark>頻寬限制為每月 100 GB</mark>。

GitHub Pages sites have a soft limit of 10 builds per hour. This limit does not apply if you build and publish your site with a custom GitHub Actions workflow.

> GitHub Pages 網站的軟限制為<mark>每小時 10 次建置</mark>。如果您使用自訂 GitHub Actions 工作流程建立和發佈站點，則此限制不適用。

In order to provide consistent quality of service for all GitHub Pages sites, rate limits may apply. These rate limits are not intended to interfere with legitimate uses of GitHub Pages. If your request triggers rate limiting, you will receive an appropriate response with an HTTP status code of 429, along with an informative HTML body.

> 為了提供一致的服務品質給所有 GitHub Pages 網站，可能存在速率限制。這些速率限制無意干擾 GitHub Pages 的合法使用。如果您的請求觸發速率限制，您將收到相應的回應，其中包含 HTTP 狀態代碼 429 以及資訊豐富的 HTML 正文。

If your site exceeds these usage quotas, we may not be able to serve your site, or you may receive a polite email from GitHub Support suggesting strategies for reducing your site's impact on our servers, including putting a third-party content distribution network (CDN) in front of your site, making use of other GitHub features such as releases, or moving to a different hosting service that might better fit your needs.

> 如果您的網站超出這些使用配額，我們可能無法為您的網站提供服務，或者您可能會收到一封來自 GitHub Support 的禮貌電子郵件，其中建議了減少您的網站對我們伺服器影響的策略，包括<mark>放置 CDN 在您的網站前面<mark>，利用其他 GitHub 功能（例如發布），或轉移到可能更適合您的需求的其他託管服務。

### Types of GitHub Pages sites 網站的類型

GitHub Pages 網站分為三種類型：
- 專案 (project)
  - 使用者個人帳號的網址會是 `http(s)://<username>.github.io/<repository>`
  - 組織帳號的網址會是 `http(s)://<organization>.github.io/<repository>`
- 使用者 (user)
  - 須建立一個名為 `<username>.github.io` 的 Repo
  - 網址會是 `http(s)://<username>.github.io`
- 組織 (organization)。
  - 須建立一個名為 `<organization>.github.io` 的 Repo
  - 網址會是 `http(s)://<organization>.github.io`

### Custom Domains 自訂網域 

- About custom domains and GitHub Pages
  - https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages
