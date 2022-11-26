from cgitb import text
from email.mime import audio
from stringprep import b3_exceptions
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import platform
import json
import pathlib
import requests
from gentle_out import *
from videoFinisher import *


# create root window
root = Tk()
# root window title and dimension
root.title("Speaking Portal")
# Set geometry (widthxheight)
root.geometry('500x500')
# launch docker container
os.system("python docker_script.py")

textPath = ""
audioPath = ""
local_path = pathlib.Path(__file__).parent.resolve().parent.resolve()
sys_info = platform.system()
if sys_info == "Darwin":
    local_path = str(local_path) + "/data/text/test.json"
else:
    local_path = str(local_path) + "\\data\\text\\test.json"

def browseTxtFile():
    global textPath
    textPath = filedialog.askopenfilename(initialdir=localpath,
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("All files",
                                                      "*.*")))
    label.configure(text="Text File Loaded!")

def browseAudioFile():
    global audioPath
    audioPath = filedialog.askopenfilename(initialdir=localpath,
                                          title="Select a File",
                                          filetypes=(("Audio Files",
                                                      "*.mp3*, *.wav*"),
                                                     ("All files",
                                                      "*.*")))
    label.configure(text="Audio File Loaded!")

def run():
    print(textPath + " " + audioPath)
    if __name__ == '__main__':
        URL = "http://localhost:8765/transcriptions?async=false"
        phoneme_list = generate_phoneme_list(URL, textPath, audioPath)
        save_phoneme_list(local_path, phoneme_list)
        generate_video(audioPath, textPath)
        exit

label = Label(root, text="", font=("Courier 10 bold"))
heading = Label(root, text="Speaking Portal - Video Generator", font=("Courier 16"), bg="white", width=65, height=5)

b_t = Button(root, text="select text file", width=30, height=2, command=browseTxtFile)
b_a = Button(root, text="select audio file", width=30, height=2, command=browseAudioFile)
b_e = Button(root, text="exit", width=30, height=2, command=exit)
b_r = Button(root, text="Generate Video", width=30, height=2, command=run)

root.columnconfigure(1, weight=1)
label.grid(column=1, row=2)
heading.grid(column=1, row=1)
b_t.grid(column=1, row=3, columnspan=2)
b_a.grid(column=1, row=4)
b_r.grid(column=1, row=5)
b_e.grid(column=1, row=6)
# all widgets will be here
# Execute Tkinter
root.mainloop()
