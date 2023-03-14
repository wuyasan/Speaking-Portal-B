import os
import sys

def JpntextConvert(filename):
    file = open(filename, "r+")
    para = file.read()
    list = para.split()
    result = " ".join(list)
    file.write(result)
    file.close()
