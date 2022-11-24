from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>INDEX PAGE!</h1>'

@app.route('/helloworld', methods=['GET'])
def hello_world():
    return 'Hello, World!'