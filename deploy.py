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
exclude = ['.git', 'docs', 'api', 'mouths', 'backgrounds', 'poses', 'data', 'src']
for root, dirs, files in os.walk(cwd):
    dirs[:] = [d for d in dirs if d not in exclude]
    for name in files:
        rootFiles.append(os.path.join(root, name))

print("\n")
    # for name in dirs:
    #     print("DIRS: " + os.path.join(root, name))

exclude = ['.git']
# Parse Mouths Directory
mouthFiles = []

for root, dirs, files in os.walk(cwd + '/mouths'):
    for name in files:
        print(name)
        mouthFiles.append(os.path.join(root, name))

print("\n")
# Parse Backgrounds Directory
backgroundFiles = []

for root, dirs, files in os.walk(cwd + '/backgrounds'):
    for name in files:
        backgroundFiles.append(os.path.join(root, name))

print("\n")
# Parse Poses Directory
poseFiles = []

for root, dirs, files in os.walk(cwd + '/poses'):
    for name in files:
        poseFiles.append(os.path.join(root, name))

print("\n")
# Parse Data Directory
dataFiles = []

for root, dirs, files in os.walk(cwd + '/data'):
    for name in files:
        dataFiles.append(os.path.join(root, name))

print("\n")
# Parse Src Directory
srcFiles = []

for root, dirs, files in os.walk(cwd + '/src'):
    print("SRC FILES: ")
    for name in files:
        srcFiles.append(os.path.join(root, name))

print("\n")
# Parse api Directory
apiFiles = []

for root, dirs, files in os.walk(cwd + '/api'):
    print("API FILES: ")
    for name in files:
        apiFiles.append(os.path.join(root, name))

# Loop through all files in the src and save paths to a list

# files = []
# for file in os.listdir(os.getcwd()):
#     # if file.endswith(".py"):
#     files.append(os.path.join(os.getcwd(), file))

# print("Files to be deployed: ")

# for file in rootFiles:
#     print(file)
# # Deploy files to GCP

file_str = ' '.join(files)
# print("Deploying files: " + file_str)
# upload_file_cmd = 'gcloud compute scp "{}" {}:Speaking-Portal-B --zone={} --project={}'.format(file_str, VM_NAME, ZONE, PROJECT)

# The first you run this command it will ask to generate a SSH key file

# pipe = os.popen(upload_file_cmd) # Will ask for ssh passphrase everytime it is run

print("Files uploaded")

exit()
