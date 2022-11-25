from flask import Flask, request, send_from_directory
import os
import requests
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

@app.route('/gentle-output', methods=['PUT'])
def gentle_output():

    default_files = False
    try:
        if(len(request.files) != 2 or 'text_file' not in request.files or 'audio_file' not in request.files):
            print("Text file not received, using default text file")
            text_file = open(app.config["SERVER_FILES"] + "/test.txt", "r")
            print("Audio file not received, using default audio file")
            audio_file = open(app.config["SERVER_FILES"] + "/test.mp3", "rb")
            default_files = True
        else:
            text_file = request.files['text_file']
            audio_file = request.files['audio_file']

        # TODO: Make gentle request
        return 'OK', 200
    except Exception as e:
        return 'FileNotReceived: {}'.format(e), 400

@app.route('/generate-video', methods=['GET'])
def video_processing():
    return 'This will return the video'

@app.route('/get-avatar', methods=['GET'])
def get_avatar():
    return 'This will return the avatar'