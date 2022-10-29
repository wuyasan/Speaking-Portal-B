import os

# Testing gcloud by opening a pipe to the command line

pipe = os.popen('gcloud --version')

# Printing the output of the command line

print(pipe.read())

