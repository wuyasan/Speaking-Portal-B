import os
from werkzeug.utils import secure_filename
import logging
from functions import returnObj
from functions.jobQueue import Job
logging.basicConfig(level=logging.INFO)

# os.mkdir(JOB_DIR)

def receive_files(text_file, audio_file, job: Job):
    logging.info("Received files and initialized job: \n" + str(job))
    job_dir = job.get_job_dir()
    inputs_dir = job_dir + "/inputs"
    job_id = job.get_job_id()
    # Read text_file received in PUT request
    text_filename = job_id + ".lab"
    # Save text_file to server and wait for it to be saved
    text_path = os.path.join(inputs_dir, text_filename)
    text_file.save(text_path)


    try:
        with open(inputs_dir + "/" + text_filename, "r", encoding='utf-8') as file:
            text = file.read()
            print("Reading text file...")
            print(text)
    except Exception as e:
        print("Error reading text file: " + str(e))
        return returnObj.error(msg="Error reading text file: " + str(e), job_id=job_id, code=500)
    
    # Read audio_file received in PUT request
    audio_filename = job_id + ".wav"
    # Save audio_file to server and wait for it to be saved
    audio_path = os.path.join(inputs_dir, audio_filename)
    audio_file.save(audio_path)

    try:
        with open(inputs_dir + "/" + audio_filename, "rb") as file:
            audio = file.read()
            print("Reading audio file...")
            # print(audio)
    except Exception as e:
        print("Error reading audio file: " + str(e))
        return returnObj.error(msg="Error reading audio file: " + str(e), job_id=job_id, code=500)

    return returnObj.success(msg="Files received successfully", data={
        "text_path": text_path,
        "audio_path": audio_path,
        "job_dir": job_dir,
        "job_id": job_id
    }, code=200)

    
