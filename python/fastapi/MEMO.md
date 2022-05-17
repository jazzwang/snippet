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