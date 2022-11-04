from stringprep import b3_exceptions
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

# create root window
root = Tk()
# root window title and dimension
root.title("Put the text in and audio out")
# Set geometry (widthxheight)
root.geometry('500x500')

label = Label(root, text="Get your file", font=("Courier 10"))


def browsetxtFile():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("All files",
                                                      "*.*")))
    label.configure(text="File Opened: "+filename)

def browseaudioFile():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Audio Files",
                                                      "*.mp3*"),
                                                     ("All files",
                                                      "*.*")))
    label.configure(text="File Opened: "+filename)

b_t = Button(root, text="select text file", width=20, command=browsetxtFile)
b_a = Button(root, text="select audio file", width=20, command=browseaudioFile)
b_e = Button(root, text="exit", width=20, command=exit)

label.grid(column=5, row=1)
b_t.grid(column=5, row=2)
b_a.grid(column=5, row=3)
b_e.grid(column=5, row=4)
# all widgets will be here
# Execute Tkinter
root.mainloop()
