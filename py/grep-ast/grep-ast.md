# grep-ast

- Git Repo
  -
  - https://github.com/paul-gauthier/grep-ast

## 2025-04-25

- 安裝
```bash
jazzw@JazzBook:~/git/snippet/py/grep-ast$ python -m pip install git+https://github.com/paul-gauthier/grep-ast.git
```
- 測試：
```
jazzw@JazzBook:~/git/confluence-insight$ which grep-ast
/c/Users/jazzw/scoop/apps/python/current/Scripts/grep-ast
jazzw@JazzBook:~/git/confluence-insight$ grep-ast node *

gen-pageGraph.py:

│# -*- coding: utf-8 -*-
│
│import os, csv
⋮
│
█nodes = {}
│
│df = pd.read_csv(space_key+"_pageHistories.csv", sep=';')
│for i in df[['contributor_id','contributor_name']].drop_duplicates().values.tolist():
█    nodes[i[0]]={ 'name' :  i[1] , 'type' : 'contributor' }
│
│for j in df['pageId'].drop_duplicates().values.tolist():
█    nodes[j]={ 'type' : 'page' }
│
│web = Web(
│    adjacency=pageLinks,
│    title=space_key,
│    display={
█        'nodes' : nodes
│    },
│)
│
⋮
│web.save(space_key+'_pageGraph.html')


get-pages.py:

│# -*- coding: utf-8 -*-
│
│import os, time
⋮
│with sync_playwright() as p:
│    browser = p.chromium.launch(headless=False)
⋮
│
█    # Expand all closed tree nodes
│    more_pages = True
│    while more_pages:
│        try:
█            node = page.query_selector(".closed .click-zone")
█            if node:
█                node.click()
│                time.sleep(0.1) # wait 100ms for UI to remove .closed status
│            else:
│                more_pages = False
│        except Exception as e:
│            more_pages = False
│            break
│
⋮
│    browser.close()

```