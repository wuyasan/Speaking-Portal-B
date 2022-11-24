from flask import Flask, request, send_from_directory
import os
app = Flask(__name__)

app.config["SERVER_FILES"] = os.getcwd() + "/server_files"

@app.route('/')
def index():
    return '<h1>INDEX PAGE!</h1>'

@app.route('/helloworld', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/text-to-speech', methods=['PUT'])
def text_to_speech():
    try:
        text_file = request.files['text_file']
        print(text_file.read().decode('utf-8'))
    except Exception as e:
        return 'FileNotReceived: {}'.format(e), 400
    
    try:
        return send_from_directory(app.config["SERVER_FILES"], "test.mp3", as_attachment=True)
    except Exception as e:
        return 'Error: {}'.format(e), 500
    

    
    

@app.route('/gentle-output', methods=['POST'])
def gentle_output():
    return 'This will return the gentle output'

@app.route('/generate-video', methods=['GET'])
def video_processing():
    return 'This will return the video'

@app.route('/get-avatar', methods=['GET'])
def get_avatar():
    return 'This will return the avatar'