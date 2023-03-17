import os
import sys
import logging
import subprocess
import shutil
logging.basicConfig(level=logging.INFO)
# Append the parent directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # src/
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) # root
from flask import Flask, request, send_from_directory
from functions import receiveFiles, returnObj, mfa, JpntextConvert, IPAtoARPA
from functions.jobQueue import JobQueue, Job, JobStatus
from src import scheduler, videoDrawer
app = Flask(__name__)
SUPPORTED_LANGUAGES = ["english", "french", "japanese"]
app.config["SERVER_FILES"] = os.getcwd() + "/server_files"
# Initialize JobQueue
job_queue = JobQueue()


# ROUTE: /generate
# METHOD: PUT
# DESCRIPTION: Receives text and audio files and generates a video
# PARAMS: text_file, audio_file, lang - see SUPPORTED_LANGUAGES
# RETURN: JSON object with status, code, data
@app.route('/generate', methods=['PUT'])
def generate():
    print("Received request to generate video")
    # Get lang from request
    lang = request.values['lang']
    if lang is None:
        lang = "english"
    
    # lang to lowercase
    lang = lang.lower()
    # Check if lang is supported
    if lang not in SUPPORTED_LANGUAGES:
        return returnObj.error(msg="Language not supported\n Select from " + str(SUPPORTED_LANGUAGES), code=400), 400
    # Receive text and audio files
    # TODO: Check file extensions is correct. If it's a .txt then convert to .lab. If it's a .mp3 then convert to .wav
    text_file = request.files['text_file']
    audio_file = request.files['audio_file']

    # Check if text_file has been received
    if text_file is None:
        return returnObj.error(msg="No text file received", code=400), 400
    # Check if audio_file has been received
    if audio_file is None:
        return returnObj.error(msg="No audio file received", code=400), 400
    else: 
        # Create a new job
        job = Job()
        # Add the job to the queue
        job_queue.add_job(job)
        # Change the status of the job to PROCESSING_FILES
        job.set_status(JobStatus.PROCESSING_FILES)
        obj = receiveFiles.receive_files(text_file, audio_file, job)
        if obj['status'] == 'error':
            # Change the status of the job to ERROR
            job.set_status(JobStatus.ERROR)
            # Remove the job from queue
            job_queue.remove_job(job_id=obj['data']['job_id'])
            return obj, obj['code']

    # TODO: Check formatting of received files

    # Run mfa validate with files

    job_dir = obj['data']['job_dir']
    inputs_dir = job_dir + "/inputs"

    if lang == "japanese":
        # Run Japanese String Separator
        logging.info("Running Japanese String Separator")
        input_path = inputs_dir + "/" + job.get_job_id() + ".lab"
        # Output path is same as input path
        obj = JpntextConvert.JpntextConvert(input_path=input_path, output_path=input_path, job=job)
        if obj['status'] == 'error':
            # Change the status of the job to ERROR
            job.set_status(JobStatus.ERROR)
            # Remove the job from queue
            job_queue.remove_job(job_id=obj['job_id'])
            return obj, obj['code']
    
    # print("Running mfa validate with job_dir: " + job_dir)
    # # Change the status of the job to MFA_VALIDATION
    # job.set_status(JobStatus.MFA_VALIDATION)
    # obj = mfa.validate(inputs_dir, job, lang=lang)
    # if obj['status'] == 'error':
    #     # Change the status of the job to ERROR
    #     job.set_status(JobStatus.ERROR)
    #     # Remove the job from queue
    #     job_queue.remove_job(job_id=obj['data']['job_id'])
    #     return obj, obj['code']
    
    # print("Time taken to validate: " + str(obj['data']['timeTaken']) + " seconds")

    # Run mfa align

    print("Running mfa align with job_dir: " + job_dir)
    # Change the status of the job to MFA_ALIGN
    job.set_status(JobStatus.MFA_ALIGN)
    obj = mfa.align(inputs_dir, job=job, lang=lang)
    # Output dir is job_dir + /outputs
    if obj['status'] == 'error':
        # Change the status of the job to ERROR
        job.set_status(JobStatus.ERROR)
        # Remove the job from queue
        job_queue.remove_job(job_id=obj['data']['job_id'])
        return obj, obj['code']
    print("Time taken to align: " + str(obj['data']['timeTaken']) + " seconds")

    # Convert french IPA to ARPA
    if lang == "french":
        logging.info("Converting french IPA to ARPA")
        mfa_json = job_queue.get_job(job_id=obj['data']['job_id']).get_job_dir() + "/outputs/" + obj["data"]["job_id"] + ".json"
        obj = IPAtoARPA.convert_IPA_to_ARPA(mfa_json, mfa_json, job=job)
        if obj['status'] == 'error':
            # Change the status of the job to ERROR
            job.set_status(JobStatus.ERROR)
            # Remove the job from queue
            job_queue.remove_job(job_id=obj['job_id'])
            return obj, obj['code']

    
    # Conver mfa output to gentle output
    # Change the status of the job to MFA_CONVERT
    job.set_status(JobStatus.MFA_CONVERTER)
    obj = mfa.converter(output_dir=job_dir + "/outputs", json_filename=job.get_job_id() + ".json", job=job)
    if obj['status'] == 'error':
        # Change the status of the job to ERROR
        job.set_status(JobStatus.ERROR)
        # Remove the job from queue
        job_queue.remove_job(job_id=obj['data']['job_id'])
        return obj, obj['code']

    # Run frame scheduler
    job = job_queue.get_job(job_id=obj['data']['job_id'])
    # Change the status of the job to FRAME_SCHEDULER
    job.set_status(JobStatus.SCHEDULING_FRAMES)
    try: 
        obj = scheduler.frame_schedule(textPath=inputs_dir + "/" + job.get_job_id() + ".lab", aligned_json_path= job_dir + "/outputs/mfa_converted.json", job=job, lang=lang.upper())
    except Exception as e:
        logging.error("Error in frame scheduler: " + str(e))
        # Change the status of the job to ERROR
        job.set_status(JobStatus.ERROR)
        # Remove the job from queue
        job_queue.remove_job(job_id=job.get_job_id())
        return returnObj.error(msg="Error in frame scheduler: " + str(e), code=500), 500
    if obj['status'] == 'error':
        # Change the status of the job to ERROR
        job.set_status(JobStatus.ERROR)
        # Remove the job from queue
        job_queue.remove_job(job_id=job.get_job_id())
        return obj, obj['code']
    
    # Run video drawer
    schedulePath =  job_dir + "/outputs/schedule.csv"
    logging.info("Running video drawer with schedulePath: " + schedulePath)
    # Change the status of the job to GENERATING_VIDEO_FRAMES
    job.set_status(JobStatus.GENERATING_VIDEO_FRAMES)
    obj = videoDrawer.runVideoDrawer(schedulePath=schedulePath, job=job)
    if obj['status'] == 'error':
        # Change the status of the job to ERROR
        job.set_status(JobStatus.ERROR)
        # Remove the job from queue
        job_queue.remove_job(job_id=obj['job_id'])
        return obj, obj['code']
    logging.info("Frames generated successfully")

    # Run video finisher command
    frames_dir = job.get_job_dir() + "/frames"
    audioPath = job.get_job_dir() + "/inputs/" + job.get_job_id() + ".wav"
    output_path = job.get_job_dir() + "/outputs"
    logging.info("Running video finisher with frames_dir: " + frames_dir + ", \naudioPath: " + audioPath + ", \noutput_path: " + output_path)
    # Change the status of the job to STITCHING_VIDEO_FRAMES
    job.set_status(JobStatus.STITCHING_VIDEO_FRAMES)
    command = "ffmpeg -r 30 -f image2 -s 1920x1080 -i " + frames_dir + "/f%06d.png -i "+ audioPath + " -vcodec libx264 -b 4M -c:a aac -strict -2 -pix_fmt yuv420p "+ output_path +"/generatedVideo.mp4 -y"
    pipe = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if pipe.returncode != 0:
        # Change the status of the job to ERROR
        job.set_status(JobStatus.ERROR)
        logging.error("Error in video finisher")
        logging.error(pipe.stderr.decode("utf-8"))
        # Remove the job from queue
        job_queue.remove_job(job_id=job.get_job_id())
        return returnObj.error(msg="Error in video finisher", code=500), 500
    else:
        shutil.rmtree(frames_dir, ignore_errors=True)
        # Change the status of the job to COMPLETED
        job.set_status(JobStatus.COMPLETED)
        # Send video file and delete job from queue
        return send_from_directory(output_path, "generatedVideo.mp4")
        # return returnObj.success(msg="Video generated successfully", data={"job_id": job.get_job_id()}), 200
