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

cwd = os.getcwd()

# Parse all files

# Parse Root Directory
rootFiles = []
exclude = ['.git', 'docs', 'api', 'mouths', 'backgrounds', 'poses', 'data', 'src', 'new_mouths', 'Team Agreement.md', 'README.md']
for root, dirs, files in os.walk(cwd):
    dirs[:] = [d for d in dirs if d not in exclude]
    for name in files:
        rootFiles.append(os.path.join(root, name))



# Parse Mouths Directory
mouthFiles = []
for root, dirs, files in os.walk(cwd + '/mouths'):
    for name in files:
        mouthFiles.append(os.path.join(root, name))

# Parse Backgrounds Directory
backgroundFiles = []
for root, dirs, files in os.walk(cwd + '/backgrounds'):
    for name in files:
        backgroundFiles.append(os.path.join(root, name))

# Parse Poses Directory
poseFiles = []

for root, dirs, files in os.walk(cwd + '/poses'):
    for name in files:
        poseFiles.append(os.path.join(root, name))

# Parse Data Directory
dataFiles = []

for root, dirs, files in os.walk(cwd + '/data'):
    for name in files:
        dataFiles.append(os.path.join(root, name))

# Parse Src Directory
srcFiles = []
exclude = ['__pycache__']
for root, dirs, files in os.walk(cwd + '/src'):
    dirs[:] = [d for d in dirs if d not in exclude]
    for name in files:
        srcFiles.append(os.path.join(root, name))

# Parse api Directory
apiFiles = []

for root, dirs, files in os.walk(cwd + '/api'):
    for name in files:
        apiFiles.append(os.path.join(root, name))

# Parse new_mouths Directory

# Loop through all files in the src and save paths to a list

files = rootFiles + srcFiles + apiFiles + dataFiles + poseFiles + mouthFiles

# print("Files to be deployed: ")

for file in rootFiles:
    print(file)
# Deploy files to GCP

file_str = ' '.join(rootFiles)
# print("Deploying files: " + file_str)
upload_file_cmd = 'gcloud compute scp {} {}:Speaking-Portal-B --zone={} --project={} --ssh-key-file=/Users/yash/.ssh/google_compute_engine'.format(file_str, VM_NAME, ZONE, PROJECT)

# The first time you run this command it will ask to generate a SSH key file
print("Cmd: " + upload_file_cmd)
# pipe = os.popen(upload_file_cmd) # Will ask for ssh passphrase everytime it is run

# print("Files uploaded")

exit()
