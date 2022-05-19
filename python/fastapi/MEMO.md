# MEMO

## Development Environment

https://fastapi.tiangolo.com/tutorial
```
~/git/snippet/python/fastapi$ pip install "fastapi[all]"
```

## 2022-05-17

- ( 2022-05-17 10:27:05 )
- https://fastapi.tiangolo.com/tutorial/first-steps/
```bash
~/git/snippet/python/fastapi$ pip install "fastapi[all]"
~/git/snippet/python/fastapi$ cat > main.py << EOF
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
EOF
~/git/snippet/python/fastapi$ uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['/Users/jazzwang/git/snippet/python/fastapi']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [42064] using watchgod
INFO:     Started server process [42066]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
- ( 2022-05-17 10:31:13 )
  - http://127.0.0.1:8000/
  - http://127.0.0.1:8000/docs
  - http://127.0.0.1:8000/redoc
  - http://127.0.0.1:8000/openapi.json

## 2022-05-18

- https://fastapi.tiangolo.com/tutorial/body/
- ( 2022-05-18 00:19:58 )
```bash
~/git/snippet/python/fastapi$ cat > pet.py << EOF
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class Pet(BaseModel):
    id: int
    name: str
    status: str

app = FastAPI()

@app.post("/pet/")
async def create_pet(pet: Pet):
    return pet
EOF
```
- ( 2022-05-18 00:21:51 )
- test POST request with JSON object
- http://127.0.0.1:8000/docs#/default/create_pet_pet__post
```
curl -X 'POST' \
  'http://127.0.0.1:8000/pet/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 0,
  "name": "string",
  "status": "string"
}'
```
- ( 2022-05-18 00:25:04 )
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/pet/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}'
```
- Response body
```json
{
  "id": 0,
  "name": "doggie",
  "status": "available"
}
```
- Response headers
```
 content-length: 45
 content-type: application/json
 date: Tue,17 May 2022 16:24:45 GMT
 server: uvicorn
```

## 2022-05-19

- ( 2022-05-19 12:50:28 )
- Q: `contract first` vs `implement first`? 目前看起來 FastAPI 的基本邏輯是 `implement first`，若要走 `contract first` 只能用 openapi-generator？
- A:
  - https://github.com/tiangolo/fastapi/issues/519 - 2019 年九月討論過
  - code generator (if following `contract first`/`spec first`)
    - https://github.com/koxudaxi/fastapi-code-generator
      - https://pypi.org/project/fastapi-code-generator/
    - https://github.com/dmontagu/fastapi_client
    - **https://openapi-generator.tech/docs/generators/python-fastapi**

- ( 2022-05-19 13:10:44 )
- https://fastapi.tiangolo.com/tutorial/testing/
- Q: 怎麼做單元測試 Unit Test？
- A: 搭配 [pytest](https://docs.pytest.org/)
- ( 2022-05-19 21:11:48 )
```
~/git/snippet/python/fastapi$ pip install pytest
~/git/snippet/python/fastapi$ cat > test_main.py << EOF
from fastapi.testclient import TestClient

from main import app
client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Hello World"}
EOF
~/git/snippet/python/fastapi$ pytest
============================== test session starts ==============================
platform darwin -- Python 3.8.9, pytest-7.1.2, pluggy-1.0.0
rootdir: /Users/jazzwang/git/snippet/python/fastapi
plugins: anyio-3.6.1
collected 1 item

test_main.py .                                                            [100%]

=============================== 1 passed in 0.60s ===============================
```
- ( 2022-05-19 21:42:40 )
- 測試 POST request
```
~/git/snippet/python/fastapi$ cat test_pet.py
from fastapi.testclient import TestClient

from pet import app

client = TestClient(app)

def test_add_pet():
  response = client.post(
      "/pet",
      headers={ "accept": "application/json", "Content-Type": "application/json" },
      json={ "id": 0, "name": "doggie", "status": "available" }
  )
  assert response.status_code == 200
  assert response.json() == { "id": 0, "name": "doggie", "status": "available" }
  EOF
  ~/git/snippet/python/fastapi$ pytest
============================= test session starts ==============================
platform darwin -- Python 3.8.9, pytest-7.1.2, pluggy-1.0.0
rootdir: /Users/jazzwang/git/snippet/python/fastapi
plugins: anyio-3.6.1
collected 2 items

test_main.py .                                                           [ 50%]
test_pet.py .                                                            [100%]

============================== 2 passed in 0.80s ===============================
```
- 注意：結尾的反斜線也有差。
```diff
diff --git a/python/fastapi/MEMO.md b/python/fastapi/MEMO.md
index 8c8736f..5a34c9a 100644
--- a/python/fastapi/MEMO.md
+++ b/python/fastapi/MEMO.md
@@ -54,7 +54,7 @@ class Pet(BaseModel):

 app = FastAPI()

-@app.post("/pet/")
+@app.post("/pet")
 async def create_pet(pet: Pet):
     return pet
```