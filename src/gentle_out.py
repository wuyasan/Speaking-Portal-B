import requests
import os
import json


URL = "http://localhost:8765/transcriptions?async=false"
audioPath = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'data', 'audio', 'test.mp3'))
textPath = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'data', 'text', 'test.txt'))
audioFile = open(audioPath, "rb")
textFile = open(textPath, "rb")
phonemeList = requests.post(
    url=URL,
    files={
        'audio': audioFile,
        'transcript': textFile
    }
)
phonemeList = phonemeList.json()
print(json.dumps(phonemeList, indent=2))


# Splits up phoneme timestamp and duration
words = phonemeList['words']
for word in words:
    wstart = word['start']
    print("\n\nWord start t-stamp = " + str(wstart))
    print("word = " + word['alignedWord'] + "\nphonemes in word = \n", end='')
    for phoneInfo in word['phones']:
        print(phoneInfo['phone'] + ", ", end='')
        wstart += phoneInfo['duration']
        print("Duration: " + str(phoneInfo['duration']) + " Phoneme end t-stamp: " + str(round(wstart,2)))
