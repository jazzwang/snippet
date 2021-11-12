# README

## Development Notes

* https://flask.palletsprojects.com/en/2.0.x/quickstart/

```
~/snippet/python/flask$ pip3 install flask
~/snippet/python/flask$ cat > hello.py << EOF
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
EOF

~/snippet/python/flask$ export FLASK_APP=hello
~/snippet/python/flask$ flask run
 * Serving Flask app 'hello' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```