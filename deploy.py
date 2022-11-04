import os

# CONSTANTS

GCLOUD_ACCOUNT = 'team.b.kukarella.capstone@gmail.com'
VM_NAME = 'instance-1'
ZONE = 'us-central1-c'
PROJECT = 'speaking-portal-b'

# Confirm logged into gcloud CLI with the correct account 

pipe = os.popen('gcloud auth list --filter=status:ACTIVE --format="value(account)"')

active_account = pipe.read().strip()

if active_account != GCLOUD_ACCOUNT:

    print('Please login to gcloud CLI with the correct account')

    # Exits process
    exit()

# Dry Run

cwd = os.getcwd() + '/src'

os.chdir(cwd)

print("In dir: " + os.getcwd())

# Loop through all files in the src and save paths to a list

files = []
for file in os.listdir(os.getcwd()):
    if file.endswith(".py"):
        files.append(os.path.join(os.getcwd(), file))

print("Files to be deployed: " + str(files))

# Deploy files to GCP

file_str = ' '.join(files)
print("Deploying files: " + file_str)
upload_file_cmd = 'gcloud compute scp "{}" {}:Speaking-Portal-B --zone={} --project={}'.format(file_str, VM_NAME, ZONE, PROJECT)

# The first you run this command it will ask to generate a SSH key file

pipe = os.popen(upload_file_cmd) # Will ask for ssh passphrase everytime it is run

print("Files uploaded")

exit()
