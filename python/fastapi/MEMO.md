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