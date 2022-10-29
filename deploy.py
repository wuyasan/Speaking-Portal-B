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

# Loop through all files in the current directory and save paths to a list

files = []
for file in os.listdir(os.getcwd()):
    if file.endswith(".py"):
        files.append(os.path.join(os.getcwd(), file))

print("Files to be deployed: " + str(files))

# Deploy files to GCP



# # The first you run this command it will ask to generate a SSH key file
# pipe = os.popen('gcloud compute scp ' + cwd + ' instance-1:~ --dry-run --project=speaking-portal-b --zone=us-central1-c')

# dry_run_output = pipe.read()

# print(dry_run_output)

exit()
