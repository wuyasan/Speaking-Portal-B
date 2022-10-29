import os

# Confirm logged into gcloud CLI with the correct account 

pipe = os.popen('gcloud auth list --filter=status:ACTIVE --format="value(account)"')

active_account = pipe.read().strip()

if active_account != 'team.b.kukarella.capstone@gmail.com':

    print('Please login to gcloud CLI with the correct account')

    # Exits process
    exit()


