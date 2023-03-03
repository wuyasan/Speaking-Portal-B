from flask import Flask, request, send_from_directory
import os
import json
from functions import receiveFiles, returnObj, mfa
app = Flask(__name__)

app.config["SERVER_FILES"] = os.getcwd() + "/server_files"

@app.route('/generate', methods=['PUT'])
def generate():
    # TODO: Receive text and audio files
    # return 'FilesReceived', 200
    text_file = request.files['text_file']
    audio_file = request.files['audio_file']
    
    # Check if files are received
    if text_file is None or audio_file is None:
        return returnObj.error(msg="No files received", code=400), 400
    else: 
        obj = receiveFiles.receive_files(text_file, audio_file)
        if obj['status'] == 'error':
            return obj, obj['code']

    # TODO: Check formatting of received files

    # TODO: Save the files to the server with job_id

    # TODO: Run mfa validate with files
    job_dir = obj['data']['job_dir']

    print("Running mfa validate with job_dir: " + job_dir)

    # obj = mfa.validate(job_dir)
    # if obj['status'] == 'error':
    #     return obj, obj['code']

    # TODO Run mfa align

    print("Running mfa align with job_dir: " + job_dir)

    obj = mfa.align(job_dir)
    # Output dir is job_dir + /output
    if obj['status'] == 'error':
        return obj, obj['code']

    # TODO: Conver mfa output to gentle output

    obj = mfa.converter(output_dir=job_dir + "/output", json_filename=text_file.filename.replace(".lab", ".json"))
    if obj['status'] == 'error':
        return obj, obj['code']
    else: 
        return obj, obj['code']

    # TODO: Run frame scheduler

    # TODO: Save frame scheduler output

    # TODO: Run video drawer

    # TODO: Run video finisher

    # TODO: Save and return video