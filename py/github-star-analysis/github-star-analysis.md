# analyze Github starred JSON with PySpark

## 2024-11-18

- 環境：Github Codespaces
```bash
@jazzwang ➜ /workspaces/snippet (master) $ cd python/
@jazzwang ➜ /workspaces/snippet/python (master) $  pip install pyspark

   ... 略 ...

Successfully built pyspark
Installing collected packages: py4j, pyspark
Successfully installed py4j-0.10.9.7 pyspark-3.5.3

@jazzwang ➜ /workspaces/snippet/python/github-star-analysis (master) $ pyspark
Python 3.10.13 (main, Apr  3 2024, 17:08:15) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
24/11/18 22:06:56 WARN Utils: Your hostname, codespaces-79437f resolves to a loopback address: 127.0.0.1; using 10.0.1.179 instead (on interface eth0)
24/11/18 22:06:56 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
24/11/18 22:06:57 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 3.5.3
      /_/

Using Python version 3.10.13 (main, Apr  3 2024 17:08:15)
Spark context Web UI available at http://ab9f0355-bfba-4c3d-a5c9-d50cd7e94af1.internal.cloudapp.net:4040
Spark context available as 'sc' (master = local[*], app id = local-1731938818757).
SparkSession available as 'spark'.
>>> df = spark.read.json('2024-11-18_jazzwang_starred.json.gz')
>>> df.printSchema()
root
 |-- allow_forking: boolean (nullable = true)
 |-- archive_url: string (nullable = true)
 |-- archived: boolean (nullable = true)
 |-- assignees_url: string (nullable = true)
 |-- blobs_url: string (nullable = true)
 |-- branches_url: string (nullable = true)
 |-- clone_url: string (nullable = true)
 |-- collaborators_url: string (nullable = true)
 |-- comments_url: string (nullable = true)
 |-- commits_url: string (nullable = true)
 |-- compare_url: string (nullable = true)
 |-- contents_url: string (nullable = true)
 |-- contributors_url: string (nullable = true)
 |-- created_at: string (nullable = true)
 |-- default_branch: string (nullable = true)
 |-- deployments_url: string (nullable = true)
 |-- description: string (nullable = true)
 |-- disabled: boolean (nullable = true)
 |-- downloads_url: string (nullable = true)
 |-- events_url: string (nullable = true)
 |-- fork: boolean (nullable = true)
 |-- forks: long (nullable = true)
 |-- forks_count: long (nullable = true)
 |-- forks_url: string (nullable = true)
 |-- full_name: string (nullable = true)
 |-- git_commits_url: string (nullable = true)
 |-- git_refs_url: string (nullable = true)
 |-- git_tags_url: string (nullable = true)
 |-- git_url: string (nullable = true)
 |-- has_discussions: boolean (nullable = true)
 |-- has_downloads: boolean (nullable = true)
 |-- has_issues: boolean (nullable = true)
 |-- has_pages: boolean (nullable = true)
 |-- has_projects: boolean (nullable = true)
 |-- has_wiki: boolean (nullable = true)
 |-- homepage: string (nullable = true)
 |-- hooks_url: string (nullable = true)
 |-- html_url: string (nullable = true)
 |-- id: long (nullable = true)
 |-- is_template: boolean (nullable = true)
 |-- issue_comment_url: string (nullable = true)
 |-- issue_events_url: string (nullable = true)
 |-- issues_url: string (nullable = true)
 |-- keys_url: string (nullable = true)
 |-- labels_url: string (nullable = true)
 |-- language: string (nullable = true)
 |-- languages_url: string (nullable = true)
 |-- license: struct (nullable = true)
 |    |-- key: string (nullable = true)
 |    |-- name: string (nullable = true)
 |    |-- node_id: string (nullable = true)
 |    |-- spdx_id: string (nullable = true)
 |    |-- url: string (nullable = true)
 |-- merges_url: string (nullable = true)
 |-- milestones_url: string (nullable = true)
 |-- mirror_url: string (nullable = true)
 |-- name: string (nullable = true)
 |-- node_id: string (nullable = true)
 |-- notifications_url: string (nullable = true)
 |-- open_issues: long (nullable = true)
 |-- open_issues_count: long (nullable = true)
 |-- owner: struct (nullable = true)
 |    |-- avatar_url: string (nullable = true)
 |    |-- events_url: string (nullable = true)
 |    |-- followers_url: string (nullable = true)
 |    |-- following_url: string (nullable = true)
 |    |-- gists_url: string (nullable = true)
 |    |-- gravatar_id: string (nullable = true)
 |    |-- html_url: string (nullable = true)
 |    |-- id: long (nullable = true)
 |    |-- login: string (nullable = true)
 |    |-- node_id: string (nullable = true)
 |    |-- organizations_url: string (nullable = true)
 |    |-- received_events_url: string (nullable = true)
 |    |-- repos_url: string (nullable = true)
 |    |-- site_admin: boolean (nullable = true)
 |    |-- starred_url: string (nullable = true)
 |    |-- subscriptions_url: string (nullable = true)
 |    |-- type: string (nullable = true)
 |    |-- url: string (nullable = true)
 |    |-- user_view_type: string (nullable = true)
 |-- permissions: struct (nullable = true)
 |    |-- admin: boolean (nullable = true)
 |    |-- maintain: boolean (nullable = true)
 |    |-- pull: boolean (nullable = true)
 |    |-- push: boolean (nullable = true)
 |    |-- triage: boolean (nullable = true)
 |-- private: boolean (nullable = true)
 |-- pulls_url: string (nullable = true)
 |-- pushed_at: string (nullable = true)
 |-- releases_url: string (nullable = true)
 |-- size: long (nullable = true)
 |-- ssh_url: string (nullable = true)
 |-- stargazers_count: long (nullable = true)
 |-- stargazers_url: string (nullable = true)
 |-- statuses_url: string (nullable = true)
 |-- subscribers_url: string (nullable = true)
 |-- subscription_url: string (nullable = true)
 |-- svn_url: string (nullable = true)
 |-- tags_url: string (nullable = true)
 |-- teams_url: string (nullable = true)
 |-- topics: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- trees_url: string (nullable = true)
 |-- updated_at: string (nullable = true)
 |-- url: string (nullable = true)
 |-- visibility: string (nullable = true)
 |-- watchers: long (nullable = true)
 |-- watchers_count: long (nullable = true)
 |-- web_commit_signoff_required: boolean (nullable = true)
```
- 如果單純要分析 `topics` 的話，用 `jq` 就夠用了
```bash
jazzw@JazzBook:~/git/snippet/python/github-star-analysis$ zcat 2024-11-18_jazzwang_starred.json.gz | jq -c .[].topics | sort -n | grep -v '\[\]'
```
- 找出 repo owner login 大於 1 的：
```bash
jazzw@JazzBook:~/git/snippet/python/github-star-analysis$ zcat 2024-11-18_jazzwang_starred.json.gz | jq -c .[].owner.login | sort -n | uniq -c |sort -nr | less | awk '{ if ($1 > 1) print $2":"$1 }'
```
