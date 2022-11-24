from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>INDEX PAGE!</h1>'

@app.route('/helloworld', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    return 'This will return the audio file'

@app.route('/gentle-output', methods=['POST'])
def gentle_output():
    return 'This will return the gentle output'

@app.route('/generate-video', methods=['GET'])
def video_processing():
    return 'This will return the video'

@app.route('/get-avatar', methods=['GET'])
def get_avatar():
    return 'This will return the avatar'