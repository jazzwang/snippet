# Github Metrics

- 在 https://github.com/jossef/jossef/blob/master/.github/workflows/metrics.yml 看到這個 metrics 的 Github template
- https://github.com/lowlighter/metrics/blob/master/.github/readme/partials/documentation/setup/action.md

## 1️. Create a GitHub personal token

- https://github.com/settings/tokens

## 2. Put your GitHub personal token in repository secrets

- https://github.com/{username}/{username}/settings/environments/new
  - 建一個 `Production` 環境
- 接著在這個 `Production` 環境中，加入 `METRICS_TOKEN` 的環境變數。把剛剛複製的 Github Personal Token 貼到 Value

## 3. Setup GitHub Action workflow

- 參考文件，建一個檔案 `.github/workflow/metrics.yml`
```yaml
name: Metrics
on:
  # Schedule daily updates
  schedule: [{cron: "0 0 * * *"}]
  # (optional) Run workflow manually
  workflow_dispatch:
  # (optional) Run workflow when pushing on master/main
  push: {branches: ["master", "main"]}
jobs:
  github-metrics:
    runs-on: ubuntu-latest
    environment: 
      name: production
    permissions:
      contents: write
    steps:
      - uses: lowlighter/metrics@latest
        with:
          token: ${{ secrets.METRICS_TOKEN }}
```
```bash
jazzw@JazzBook:~/git/jazzwang$ mkdir -p .github/workflows/
jazzw@JazzBook:~/git/jazzwang$ code .github/workflows/metrics.yml
jazzw@JazzBook:~/git/jazzwang$ git add .github/workflows/metrics.yml
jazzw@JazzBook:~/git/jazzwang$ git commit -a -m "feat: add github action to generate github metrics."
jazzw@JazzBook:~/git/jazzwang$ git push
```
- 手動跑一次 Github Actions
  - https://github.com/jazzwang/jazzwang/actions/workflows/metrics.yml
- 執行成功後會產生 `github-metrics.svg` 所以要在 README.md 裡加上
```markdown
![Metrics](/github-metrics.svg)
```