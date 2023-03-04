import os
from werkzeug.utils import secure_filename
from functions import returnObj

SERVER_FILES_PATH = os.getcwd() + "/server_files"
JOB_DIR = os.getcwd() + "/server_files" + "/job"
# os.mkdir(JOB_DIR)

def receive_files(text_file, audio_file):
    print("JOB_DIR: " + JOB_DIR)
    # Read text_file received in PUT request
    text_filename = secure_filename(text_file.filename)
    # Save text_file to server and wait for it to be saved
    text_path = os.path.join(JOB_DIR, text_filename)
    text_file.save(text_path)


    try:
        with open(JOB_DIR + "/" + text_filename, "r", encoding='utf-8') as file:
            text = file.read()
            print("Reading text file...")
            print(text)
    except Exception as e:
        print("Error reading text file: " + str(e))
        return returnObj.error(msg="Error reading text file: " + str(e))
    
    # Read audio_file received in PUT request
    audio_filename = secure_filename(audio_file.filename)
    # Save audio_file to server and wait for it to be saved
    audio_path = os.path.join(JOB_DIR, audio_filename)
    audio_file.save(audio_path)

    try:
        with open(JOB_DIR + "/" + audio_filename, "rb") as file:
            audio = file.read()
            print("Reading audio file...")
            # print(audio)
    except Exception as e:
        print("Error reading audio file: " + str(e))
        return returnObj.error(msg="Error reading audio file: " + str(e))

    return returnObj.success(msg="Files received successfully", data={
        "text_path": text_path,
        "audio_path": audio_path,
        "job_dir": JOB_DIR
    })

    
