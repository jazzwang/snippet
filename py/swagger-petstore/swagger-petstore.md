# DEVELOPMENT MEMO

[TOC]

## 專案範本

- ( 2022-05-04 16:30:31 )
- How to create a template using [openapi-generator-cli](https://openapi-generator.tech/#try=)
- https://openapi-generator.tech/#try=
- https://openapi-generator.tech/docs/generators/python-flask/
```
~/snippet/python/swagger-petstore$ docker run --rm \
   -v $PWD:/local openapitools/openapi-generator-cli generate \
  -i https://petstore.swagger.io/v2/swagger.json \
  -g python-flask \
  -o /local
```

## 測試範本

- ( 2022-05-04 21:21:28 )
```bash
jazzwang:~/git/snippet/python/swagger-petstore$ source ~/venv/bin/activate
(venv) jazzwang:~/git/snippet/python/swagger-petstore$ pip3 install -r requirements.txt
(venv) jazzwang:~/git/snippet/python/swagger-petstore$ python3 -m openapi_server
Traceback (most recent call last):
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/runpy.py", line 194, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/Users/jazzwang/git/snippet/python/swagger-petstore/openapi_server/__main__.py", line 5, in <module>
    from openapi_server import encoder
  File "/Users/jazzwang/git/snippet/python/swagger-petstore/openapi_server/encoder.py", line 1, in <module>
    from connexion.apps.flask_app import FlaskJSONEncoder
  File "/Users/jazzwang/venv/lib/python3.8/site-packages/connexion/apps/flask_app.py", line 11, in <module>
    import flask
  File "/Users/jazzwang/venv/lib/python3.8/site-packages/flask/__init__.py", line 14, in <module>
    from jinja2 import escape
ImportError: cannot import name 'escape' from 'jinja2' (/Users/jazzwang/venv/lib/python3.8/site-packages/jinja2/__init__.py)
```
- ( 2022-05-04 21:22:25 )
- 前陣子在測試 [openxc-vehicle-simulator](https://github.com/openxc/openxc-vehicle-simulator ) 的時候，好像也有撞到 Flask 的版本相容問題。
- ( 2022-05-04 21:41:35 )
- 試著拿掉版本的限制，並用新的 venv 來驗證
```
(venv) jazzwang:~/git/snippet/python/swagger-petstore$ deactivate
jazzwang:~/git/snippet/python/swagger-petstore$ python3 -m venv venv
jazzwang:~/git/snippet/python/swagger-petstore$ source venv/bin/activate
(venv) jazzwang:~/git/snippet/python/swagger-petstore$ pip3 list
Package    Version
---------- -------
pip        20.2.3
setuptools 49.2.1
WARNING: You are using pip version 20.2.3; however, version 22.0.4 is available.
You should consider upgrading via the '/Users/jazzwang/git/snippet/python/swagger-petstore/venv/bin/python3 -m pip install --upgrade pip' command.
(venv) jazzwang:~/git/snippet/python/swagger-petstore$ python3 -m pip install --upgrade pip
(venv) jazzwang:~/git/snippet/python/swagger-petstore$ pip3 list
Package    Version
---------- -------
pip        22.0.4
setuptools 49.2.1
(venv) jazzwang:~/git/snippet/python/swagger-petstore$ cp requirements.txt new-requirements.txt
(venv) jazzwang:~/git/snippet/python/swagger-petstore$ code new-requirements.txt
(venv) jazzwang:~/git/snippet/python/swagger-petstore$ cat new-requirements.txt
connexion
swagger-ui-bundle
python_dateutil
setuptools
Flask
(venv) jazzwang:~/git/snippet/python/swagger-petstore$ pip3 install -r new-requirements.txt
(venv) jazzwang:~/git/snippet/python/swagger-petstore$ pip3 list
Package            Version
------------------ -------
click              8.1.3
Flask              2.1.2
importlib-metadata 4.11.3
itsdangerous       2.1.2
Jinja2             3.1.2
MarkupSafe         2.1.1
pip                22.0.4
python-dateutil    2.8.2
setuptools         49.2.1
six                1.16.0
swagger-ui-bundle  0.0.9
Werkzeug           2.1.2
zipp               3.8.0
(venv) jazzwang:~/git/snippet/python/swagger-petstore$ python3 -m openapi_server
this operation accepts multiple content types, using application/json
this operation accepts multiple content types, using application/json
this operation accepts multiple content types, using application/json
this operation accepts multiple content types, using application/json
this operation accepts multiple content types, using application/json
this operation accepts multiple content types, using application/json
this operation accepts multiple content types, using application/json
this operation accepts multiple content types, using application/json
 * Serving Flask app '__main__' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:8080
 * Running on http://192.168.1.103:8080 (Press CTRL+C to quit)
127.0.0.1 - - [04/May/2022 21:44:36] "GET / HTTP/1.1" 404 -
127.0.0.1 - - [04/May/2022 21:44:38] "GET /favicon.ico HTTP/1.1" 404 -
```
- ==成功！！==
- ( 2022-05-04 21:46:35 )
- 覆蓋掉舊的 `requirements.txt`
```
jazzwang:~/git/snippet/python/swagger-petstore$ mv new-requirements.txt requirements.txt
```

## 驗證範本

- ( 2022-05-04 21:52:29 )
- 測試 http://localhost:8080/v2/ui/
- 測試 http://localhost:8080/v2/openapi.json
- ==成功==
- ( 2022-05-04 22:02:49 )
- 測試 http://localhost:8080/v2/ui/#/pet/add_pet
- ==失敗==
```
jazzwang:~/git/snippet/python/swagger-petstore$ curl -X 'POST' \
>   'http://localhost:8080/v2/pet' \
>   -H 'accept: */*' \
>   -H 'Content-Type: application/json' \
>   -d '{
>   "category": {
>     "id": 6,
>     "name": "name"
>   },
>   "id": 0,
>   "name": "doggie",
>   "photoUrls": [
>     "photoUrls",
>     "photoUrls"
>   ],
>   "status": "available",
>   "tags": [
>     {
>       "id": 1,
>       "name": "name"
>     },
>     {
>       "id": 1,
>       "name": "name"
>     }
>   ]
> }'
{
  "detail": "No authorization token provided",
  "status": 401,
  "title": "Unauthorized",
  "type": "about:blank"
}
```
- ( 2022-05-04 22:05:25 )
- 用 `tox` 跑
```
jazzwang:~/git/snippet/python/swagger-petstore$ source venv/bin/activate
(venv) jazzwang:~/git/snippet/python/swagger-petstore$ pip3 install tox
(venv) jazzwang:~/git/snippet/python/swagger-petstore$ tox
```
- ==失敗==
```
(venv) jazzwang:~/git/snippet/python/swagger-petstore$ tox
py3 installed: atomicwrites==1.4.0,attrs==21.4.0,certifi==2021.10.8,charset-normalizer==2.0.12,click==8.1.3,clickclick==20.10.2,connexion==2.13.1,coverage==6.3.2,Flask==2.1.2,Flask-Testing==0.8.0,idna==3.3,importlib-metadata==4.11.3,importlib-resources==5.7.1,inflection==0.5.1,itsdangerous==2.1.2,Jinja2==3.1.2,jsonschema==4.4.0,MarkupSafe==2.1.1,more-itertools==8.12.0,openapi-server @ file:///Users/jazzwang/git/snippet/python/swagger-petstore,packaging==21.3,pluggy==0.13.1,py==1.11.0,pyparsing==3.0.8,pyrsistent==0.18.1,pytest==4.6.11,pytest-cov==3.0.0,pytest-randomly==1.2.3,python-dateutil==2.8.2,PyYAML==6.0,requests==2.27.1,six==1.16.0,swagger-ui-bundle==0.0.9,tomli==2.0.1,urllib3==1.26.9,wcwidth==0.2.5,Werkzeug==2.1.2,zipp==3.8.0
py3 run-test-pre: PYTHONHASHSEED='1349920351'
py3 run-test: commands[0] | pytest --cov=openapi_server
====================================================== test session starts =======================================================
platform darwin -- Python 3.8.9, pytest-4.6.11, py-1.11.0, pluggy-0.13.1
cachedir: .tox/py3/.pytest_cache
Using --randomly-seed=1651673869
rootdir: /Users/jazzwang/git/snippet/python/swagger-petstore
plugins: randomly-1.2.3, cov-3.0.0
collected 0 items / 3 errors

============================================================= ERRORS =============================================================
__________________________________ ERROR collecting openapi_server/test/test_pet_controller.py ___________________________________
ImportError while importing test module '/Users/jazzwang/git/snippet/python/swagger-petstore/openapi_server/test/test_pet_controller.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
openapi_server/test/__init__.py:4: in <module>
    from flask_testing import TestCase
.tox/py3/lib/python3.8/site-packages/flask_testing/__init__.py:13: in <module>
    from .utils import TestCase, LiveServerTestCase
.tox/py3/lib/python3.8/site-packages/flask_testing/utils.py:38: in <module>
    from flask import json_available, templating, template_rendered
E   ImportError: cannot import name 'json_available' from 'flask' (/Users/jazzwang/git/snippet/python/swagger-petstore/.tox/py3/lib/python3.8/site-packages/flask/__init__.py)
_________________________________ ERROR collecting openapi_server/test/test_store_controller.py __________________________________
ImportError while importing test module '/Users/jazzwang/git/snippet/python/swagger-petstore/openapi_server/test/test_store_controller.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
openapi_server/test/__init__.py:4: in <module>
    from flask_testing import TestCase
.tox/py3/lib/python3.8/site-packages/flask_testing/__init__.py:13: in <module>
    from .utils import TestCase, LiveServerTestCase
.tox/py3/lib/python3.8/site-packages/flask_testing/utils.py:38: in <module>
    from flask import json_available, templating, template_rendered
E   ImportError: cannot import name 'json_available' from 'flask' (/Users/jazzwang/git/snippet/python/swagger-petstore/.tox/py3/lib/python3.8/site-packages/flask/__init__.py)
__________________________________ ERROR collecting openapi_server/test/test_user_controller.py __________________________________
ImportError while importing test module '/Users/jazzwang/git/snippet/python/swagger-petstore/openapi_server/test/test_user_controller.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
openapi_server/test/__init__.py:4: in <module>
    from flask_testing import TestCase
.tox/py3/lib/python3.8/site-packages/flask_testing/__init__.py:13: in <module>
    from .utils import TestCase, LiveServerTestCase
.tox/py3/lib/python3.8/site-packages/flask_testing/utils.py:38: in <module>
    from flask import json_available, templating, template_rendered
E   ImportError: cannot import name 'json_available' from 'flask' (/Users/jazzwang/git/snippet/python/swagger-petstore/.tox/py3/lib/python3.8/site-packages/flask/__init__.py)

---------- coverage: platform darwin, python 3.8.9-final-0 -----------
Name                                                 Stmts   Miss  Cover
------------------------------------------------------------------------
openapi_server/__init__.py                               0      0   100%
openapi_server/__main__.py                               9      9     0%
openapi_server/controllers/__init__.py                   0      0   100%
openapi_server/controllers/pet_controller.py            28     28     0%
openapi_server/controllers/security_controller_.py       7      7     0%
openapi_server/controllers/store_controller.py          17     17     0%
openapi_server/controllers/user_controller.py           31     31     0%
openapi_server/encoder.py                               16     16     0%
openapi_server/models/__init__.py                        7      7     0%
openapi_server/models/api_response.py                   33     33     0%
openapi_server/models/base_model_.py                    31     31     0%
openapi_server/models/category.py                       26     26     0%
openapi_server/models/order.py                          57     57     0%
openapi_server/models/pet.py                            65     65     0%
openapi_server/models/tag.py                            26     26     0%
openapi_server/models/user.py                           68     68     0%
openapi_server/test/__init__.py                         11      8    27%
openapi_server/test/test_pet_controller.py              52     52     0%
openapi_server/test/test_store_controller.py            26     26     0%
openapi_server/test/test_user_controller.py             46     46     0%
openapi_server/typing_utils.py                          15     15     0%
openapi_server/util.py                                  60     60     0%
------------------------------------------------------------------------
TOTAL                                                  631    628     1%

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 3 errors during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
==================================================== 3 error in 3.03 seconds =====================================================
ERROR: InvocationError for command /Users/jazzwang/git/snippet/python/swagger-petstore/.tox/py3/bin/pytest --cov=openapi_server (exited with code 2)
____________________________________________________________ summary _____________________________________________________________
ERROR:   py3: commands failed
(venv) jazzwang:~/git/snippet/python/swagger-petstore$
```