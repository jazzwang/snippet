# MEMO

## 2022-12-27

### 緣起

- 先前分析了 Confluence Wiki 的貢獻度，也可以分析 Jira 的貢獻度。那麼 Gitlab 的貢獻度呢？
- 除了靠 Selenium 去撈 Gitlab 資料外，可否透過 Gitlab API 去分析一些開發者之間的關聯呢？

### 參考網址

- https://docs.gitlab.com/ee/api/ - Gitlab Enterprise API Doc

| package | SourceRank | version |
|---------|------------|---------|
| [python-gitlab (PyPI)](https://libraries.io/pypi/python-gitlab) | 19 | 3.6.0 |
| [python-gitlab (conda)](https://libraries.io/conda/python-gitlab) | 15 | 3.11.0 |
| [python-gitlab-api](https://libraries.io/pypi/python-gitlab-api) | 5 | 0.2.32 |

- 看起來比較成熟的是 [python-gitlab](https://github.com/python-gitlab/python-gitlab)
- 說明文件：https://python-gitlab.readthedocs.io/en/stable/
- 看起來是 Siemens 內部的開發者開始的實作 - https://www.youtube.com/watch?v=PA0sx60Epn4