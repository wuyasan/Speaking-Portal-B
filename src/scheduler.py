import argparse
from os import path
import os.path
import json
import numpy as np
import random
import pathlib
import logging
logging.basicConfig(level=logging.INFO)
from phoneToMouthMap import getMouthDict
localpath = pathlib.Path(__file__).parent.resolve().parent.resolve()
print("Scheduler.py localpath: "+str(localpath))
logging.info("Scheduler.py localpath: "+str(localpath))


def addPhoneme(p, t):
    global prevPhoneme
    global f
    if p != prevPhoneme:
        strings[4] += (str.format('{0:.3f}', t)+",phoneme,"+p+"\n")
    prevPhoneme = p


def pickNewPose(t):
    global pose
    global prevPose
    global prevPhoneme
    global newPose

    while newPose == -1 or newPose == pose or newPose == prevPose:
        newPose = int(random.random()*POSE_COUNT)
    prevPose = pose
    pose = newPose
    strings[3] += (str.format('{0:.3f}', t)+",pose,"+str(pose)+"\n")
    prevPhoneme = "na"

def assignPhoneToMouth(phone: str, mouths: dict):
    logging.info("Assiging phone: " + str(phone) + " to mouth")
    # Remove any stress marks
    phone = phone.replace("1", "")
    phone = phone.replace("2", "")
    phone = phone.replace("0", "")

    # Lowercase
    phone = phone.lower()

    # If the phone is in the map, return the mouth
    if phone in mouths:
        return mouths[phone]
    else:
        # If the phone is not in the map, return the mouth for "oov"
        return mouths["oov"]
    



def frame_schedule(textPath, aligned_json_path, job, lang="ENGLISH"):
    logging.info("TextPath in frame_schedule: "+str(textPath))
    logging.info("aligned_json_path in frame_schedule: "+str(aligned_json_path))
    logging.info("job in frame_schedule: "+str(job.get_job()))
    global strings
    global pose
    global prevPose
    global prevPhoneme
    global newPose
    global POSE_COUNT

    POSE_COUNT = 5
    pose = -1
    prevPose = -1
    newPose = -1

    strings = [""]*5

    emotions = {}
    emotions["explain"] = 0
    emotions["happy"] = 1
    emotions["sad"] = 2
    emotions["angry"] = 3
    emotions["confused"] = 4
    emotions["rq"] = 5

    mouths = getMouthDict(lang)

    ENDING_PHONEME = "m"
    STOPPERS = [",", ";", ".", ":", "!", "?"]

    # parser = argparse.ArgumentParser(description='blah')
    # parser.add_argument('--input_file', type=str,  help='the script')
    # args = parser.parse_args()
    # INPUT_FILE = args.input_file
    # logging.info("INPUT_FILE in frame_schedule: "+str(INPUT_FILE))

    # Load the text_file provided by user
    f = open(textPath, "r+")
    originalScript = f.read()
    f.close()
    # Making it uppercase avoids ValueError in originalScript.index(wordString, OS_IndexAt)+len(wordString) as the wordString obtained from json is uppercase
    originalScript = originalScript.upper()
    logging.info("Loaded original script: \n"+str(originalScript))

    #if(path.exists(str(localpath)+"/data/text/mfa2gentle.json")): 
        #print("MFA")   #if MFA is detected use MFA json
        #f = open(str(localpath)+"/data/text/mfa2gentle.json", "r+")
        #fileData = f.read()
        #f.close()
    #else:
       # print("Gentle")                                             #if no MFA use gentle json
    
    # Load the converted aligned json file
    f = open(aligned_json_path, "r")
    fileData = f.read()
    f.close()

    data = json.loads(fileData)
    WORD_COUNT = len(data['words'])

    
    prevPhoneme = "na"
    emotion = "0"
    pararaph = 0
    image = 0

    OS_IndexAt = 0
    pickNewPose(0)
    strings[1] += "0,emotion,0\n"
    strings[0] += "0,paragraph,0\n"
    strings[2] += "0,image,0\n"
    strings[4] += "0,phoneme,m\n"
    for i in range(WORD_COUNT):
        word = data['words'][i]
        logging.info("Scheduling Word: "+str(word))
        if "start" not in word:
            continue
        wordString = word["word"]
        timeStart = word["start"]
        
        OS_nextIndex = originalScript.index(wordString, OS_IndexAt)+len(wordString)
        logging.info("OS_nextIndex: "+str(OS_nextIndex))
        if "<" in originalScript[OS_IndexAt:]:
            logging.info("Found < in originalScript ")
            tagStart = originalScript.index("<", OS_IndexAt)
            tagEnd = originalScript.index(">", OS_IndexAt)
            logging.info("Tag `<` at index: "+str(tagStart))
            logging.info("Tag `>` at index: "+str(tagEnd))
            if OS_nextIndex > tagStart and tagEnd >= OS_nextIndex:
                logging.info("Tag is in word" + str(wordString))
                OS_nextIndex = originalScript.index(
                    wordString, tagEnd)+len(wordString)
                logging.info("OS_nextIndex: "+str(OS_nextIndex))
        nextDigest = originalScript[OS_IndexAt:OS_nextIndex]
        logging.info("NextDigest: "+str(nextDigest))

        if "\n" in nextDigest and data['words'][i-1]['case'] != 'not-found-in-audio' and (prevPhoneme == "a" or prevPhoneme == "f" or prevPhoneme == "u" or prevPhoneme == "y"):
            addPhoneme("m", data['words'][i-1]["end"])

        """print(wordString)
        print(str(OS_IndexAt)+", "+str(OS_nextIndex))
        print(nextDigest)
        print("")"""
        pickedPose = False
        
        # Changing posing based on punctuation in the script
        for stopper in STOPPERS:
            if stopper in nextDigest:
                pickNewPose(timeStart)
                pickedPose = True

        if "<" in nextDigest:
            logging.info("Found < in nextDigest: " + str(nextDigest))
            leftIndex = nextDigest.index("<")+1
            logging.info("leftIndex of < in nextDigest: "+str(leftIndex))
            rightIndex = nextDigest.index(">")
            logging.info("rightIndex of > in nextDigest: "+str(rightIndex))
            emotion = emotions[nextDigest[leftIndex:rightIndex]]
            strings[1] += (str.format('{0:.3f}', timeStart) +
                        ",emotion,"+str(emotion)+"\n")
            prevPhoneme = "na"

        if "\n\n" in nextDigest:
            pararaph += 1
            # The line of the script advances 2 lines whenever we hit a /n/n.
            image += 1
            strings[0] += (str.format('{0:.3f}', timeStart) +
                        ",paragraph,"+str(pararaph)+"\n")
            prevPhoneme = "na"

        if "\n" in nextDigest:
            image += 1
            strings[2] += (str.format('{0:.3f}',
                        timeStart)+",image,"+str(image)+"\n")
            prevPhoneme = "na"
            if not pickedPose:
                # A new image means we also need to have a new pose
                pickNewPose(timeStart)

        phones = word["phones"]
        timeAt = timeStart
        logging.info("Scheduling phones for word: "+str(wordString))
        logging.info("Phones: "+str(phones))
        logging.info("TimeStart: "+str(timeStart))
        for phone in phones:
            timeAt += phone["duration"]
            phoneString = phone["phone"]

            truePhone = assignPhoneToMouth(phone=phoneString, mouths=mouths)
            if len(truePhone) == 2:
                logging.info("Adding 2 phonemes: "+str(truePhone))
                addPhoneme(truePhone[0], timeAt-phone["duration"])
                addPhoneme(truePhone[1], timeAt-phone["duration"]*0.5)
            else:
                logging.info("Adding 1 phoneme: "+str(truePhone))
                addPhoneme(truePhone, timeAt-phone["duration"])
        logging.info("Done scheduling phones for word: "+str(wordString))
        OS_IndexAt = OS_nextIndex
        logging.info("Shifted OS_IndexAt to: "+str(OS_IndexAt))

    
    
    # Write the schedule to outputs dir of job
    logging.info("Writing schedule to file " + job.get_job_dir() + "/outputs/schedule.csv")
    f = open(job.get_job_dir() + "/outputs/schedule.csv", "w+")
    for i in range(len(strings)):
        f.write(strings[i])
        if i < len(strings)-1:
            f.write("SECTION\n")
    f.flush()
    f.close()
    logging.info("RAN SCHEDULER SUCCESSFULLY")
    return {
        "status": "success",
        "message": "RAN SCHEDULER SUCCESSFULLY",
        "code": 200
    }
