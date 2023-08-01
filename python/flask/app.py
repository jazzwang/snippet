from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/api/users')
def users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    data = response.json()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
