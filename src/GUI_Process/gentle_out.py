import requests
import os
import platform
import json
import pathlib


def generate_phoneme_list(URL, text_path, audio_path):
    try:
        with open(audio_path, "rb") as audio_file, open(text_path, "rb") as text_file:
            print("files loaded. generating phonemes...")
            phoneme_list = requests.post(
                url=URL,
                files={
                    'audio': audio_file,
                    'transcript': text_file
                }
            )
            print("generated list")
            return phoneme_list
    except Exception:
        "Couldn't Open file(s)..."


def print_phoneme_list(phoneme_list):
    phoneme_list = phoneme_list.json()
    print(json.dumps(phoneme_list, indent=2))


def save_phoneme_list(local_path):
    try:
        with open(local_path, "w") as outfile:
            json.dump(phoneme_list, outfile)
    except Exception:
        "Couldn't save file..."


# Splits up phoneme timestamp and duration
def print_phoneme_sequence(phoneme_list):
    phoneme_list = phoneme_list.json()
    words = phoneme_list['words']
    for word in words:
        wstart = word['start']
        print("\n\nWord start t-stamp = " + str(wstart))
        print("word = " + word['alignedWord'] + "\nphonemes in word = \n", end='')
        for phone_info in word['phones']:
            print(phone_info['phone'] + ", ", end='')
            wstart += phone_info['duration']
            print("Duration: " + str(phone_info['duration']) + " Phoneme end t-stamp: " + str(round(wstart, 2)))


if __name__ == '__main__':
    URL = "http://localhost:8765/transcriptions?async=false"
    audio_path = os.path.realpath(os.path.join(
        os.path.dirname(__file__), '..', 'data', 'audio', 'test.wav'))
    text_path = os.path.realpath(os.path.join(
        os.path.dirname(__file__), '..', 'data', 'text', 'test.txt'))
    local_path = pathlib.Path(__file__).parent.resolve().parent.resolve()
    sys_info = platform.system()
    if sys_info == "Darwin":
        local_path = str(local_path) + "/data/text/test.json"
    else:
        local_path = str(local_path) + "\\data\\text\\test.json"
    phoneme_list = generate_phoneme_list(URL, text_path, audio_path)
    print_phoneme_list(phoneme_list)
    save_phoneme_list(local_path)
    print_phoneme_sequence(phoneme_list)