import os

# CONSTANTS

GCLOUD_ACCOUNT = 'team.b.kukarella.capstone@gmail.com'
VM_NAME = 'instance-1'
USERNAME = 'yash'
EX_IP = '34.27.118.140'
ZONE = 'us-central1-c'
PROJECT = 'speaking-portal-b'

# Confirm logged into gcloud CLI with the correct account 

pipe = os.popen('gcloud auth list --filter=status:ACTIVE --format="value(account)"')

active_account = pipe.read().strip()

if active_account != GCLOUD_ACCOUNT:

    print('Please login to gcloud CLI with the correct account')

    # Exits process
    exit()

cwd = os.getcwd()

# Parse all files

# Parse Root Directory
rootFiles = []
exclude = ['.git', 'docs', 'api', 'mouths', 'backgrounds', 'poses', 'data', 'src', 'new_mouths', 'Team-Agreement.md', 'README.md']
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


# Upload root files
files_str = ' '.join(rootFiles)
print("Deploying Root files: " + files_str)
cmd = 'scp -i /Users/yash/.ssh/google_compute_engine {} {}@{}:~/Speaking-Portal-B'.format(files_str, USERNAME, EX_IP)
pipe = os.popen(cmd)
pipe.close()

# Upload mouths files
files_str = ' '.join(mouthFiles)
print("Deploying Mouths files: " + files_str)
cmd = 'scp -i /Users/yash/.ssh/google_compute_engine {} {}@{}:~/Speaking-Portal-B/mouths'.format(files_str, USERNAME, EX_IP)
pipe = os.popen(cmd)
pipe.close()

# Upload backgrounds files
files_str = ' '.join(backgroundFiles)
print("Deploying Backgrounds files: " + files_str)
cmd = 'scp -i /Users/yash/.ssh/google_compute_engine {} {}@{}:~/Speaking-Portal-B/backgrounds'.format(files_str, USERNAME, EX_IP)
pipe = os.popen(cmd)
pipe.close()

# Upload poses files
files_str = ' '.join(poseFiles)
print("Deploying Poses files: " + files_str)
cmd = 'scp -i /Users/yash/.ssh/google_compute_engine {} {}@{}:~/Speaking-Portal-B/poses'.format(files_str, USERNAME, EX_IP)
pipe = os.popen(cmd)
pipe.close()

# Upload src files
files_str = ' '.join(srcFiles)
print("Deploying Src files: " + files_str)
cmd = 'scp -i /Users/yash/.ssh/google_compute_engine {} {}@{}:~/Speaking-Portal-B/src'.format(files_str, USERNAME, EX_IP)
pipe = os.popen(cmd)
pipe.close()

# Upload api files
files_str = ' '.join(apiFiles)
print("Deploying Api files: " + files_str)
cmd = 'scp -i /Users/yash/.ssh/google_compute_engine {} {}@{}:~/Speaking-Portal-B/api'.format(files_str, USERNAME, EX_IP)
pipe = os.popen(cmd)
pipe.close()

# Upload data files
files_str = ' '.join(dataFiles)
print("Deploying Data files: " + files_str)
cmd = 'scp -i /Users/yash/.ssh/google_compute_engine {} {}@{}:~/Speaking-Portal-B/data'.format(files_str, USERNAME, EX_IP)
pipe = os.popen(cmd)
pipe.close()

exit()
