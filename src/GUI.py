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


# create root window
root = Tk()
# root window title and dimension
root.title("Put the text in and audio out")
# Set geometry (widthxheight)
root.geometry('500x500')

label = Label(root, text="Get your file", font=("Courier 10"))

textPath = ""
audioPath = ""

def browseTxtFile():
    global textPath
    textPath = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("All files",
                                                      "*.*")))
    label.configure(text="File Opened: "+textPath)

def browseAudioFile():
    global audioPath
    audioPath = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Audio Files",
                                                      "*.mp3*"),
                                                     ("All files",
                                                      "*.*")))
    label.configure(text="File Opened: "+audioPath)

def run():
    print(textPath + " " + audioPath)
    if __name__ == '__main__':
        URL = "http://localhost:8765/transcriptions?async=false"
        local_path = pathlib.Path(__file__).parent.resolve().parent.resolve()
        sys_info = platform.system()
        if sys_info == "Darwin":
            local_path = str(local_path) + "/data/text/test.json"
        else:
            local_path = str(local_path) + "\\data\\text\\test.json"
        phoneme_list = generate_phoneme_list(URL, textPath, audioPath)
        print_phoneme_list(phoneme_list)
        save_phoneme_list(local_path)
        print_phoneme_sequence(phoneme_list)

b_t = Button(root, text="select text file", width=20, command=browseTxtFile)
b_a = Button(root, text="select audio file", width=20, command=browseAudioFile)
b_e = Button(root, text="exit", width=20, command=exit)
b_r = Button(root, text="get the video", width=20, command=run)

label.grid(column=5, row=1)
b_t.grid(column=5, row=2)
b_a.grid(column=5, row=3)
b_r.grid(column=5, row=4)
b_e.grid(column=5, row=5)
# all widgets will be here
# Execute Tkinter
root.mainloop()
