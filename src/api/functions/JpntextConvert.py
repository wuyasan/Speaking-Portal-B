import os
import sys

def JpntextConvert(filename):
    file = open(filename, "r+")
    para = file.read()
    result = " ".join(list(para))
    file.write(result)
    file.close()
