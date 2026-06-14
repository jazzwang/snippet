# osv-scanner

> Vulnerability scanner written in Go which uses the data provided by https://osv.dev

- Git Repo
  - https://github.com/google/osv-scanner
- Website
  - https://google.github.io/osv-scanner/

## 2026-06-14

- Learn from https://osv.dev/#use-vulnerability-scanner
- 安裝
```bash
go install github.com/google/osv-scanner/v2/cmd/osv-scanner@v2
```
- 掃描 - Scan directory recursively
```bash
osv-scanner -r path/to/your/project
```
- 修補建議
  - Guided Remediation (basic)
```bash
osv-scanner fix --non-interactive --strategy=in-place -L path/to/package-lock.json
osv-scanner fix --non-interactive --strategy=relock -M path/to/package.json -L path/to/package-lock.json
```
  - Guided Remediation (interactive)
```bash
osv-scanner fix -M path/to/package.json -L path/to/package-lock.json
```
- 掃描容器映像檔 Scan container image
```bash
osv-scanner scan image --serve alpine:3.12
```