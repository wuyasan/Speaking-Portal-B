import os
import json
import subprocess
import time
from functions import returnObj
from functions.jobQueue import Job

models = {
    "english": {"dictionary": "english_us_arpa", "acoustic_model": "english_us_arpa"},
    "japanese": {"dictionary": "japanese_mfa", "acoustic_model": "japanese_mfa"}
}


def validate(input_dir, job: Job, lang="english"):
    start = time.time()
    # Run mfa validate subprocess
    pipe = subprocess.run(
        "mfa validate --clean {} {} {}".format(
            input_dir, models[lang]["dictionary"], models[lang]["acoustic_model"]
        ),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # Check if subprocess ran successfully
    if pipe.returncode != 0:
        end = time.time()
        print("Error running mfa validate: " + pipe.stderr.decode("utf-8"))
        return returnObj.error(
            msg="Error running mfa validate: " + pipe.stderr.decode("utf-8"),
            code=500,
            data={
                "timeTaken": end - start,
                "job_id": job.get_job_id(),
            },
        )
    else:
        end = time.time()
        print("mfa validate ran successfully, printing output: ")
        print(pipe.stdout.decode("utf-8"))
        return returnObj.success(
            msg="mfa validate ran successfully",
            code=200,
            data={
                "timeTaken": end - start,
                "job_id": job.get_job_id(),
            },
        )


def align(input_dir, job: Job, lang="english"):
    # Run mfa align subprocess
    start = time.time()
    pipe = subprocess.run(
        "mfa align --clean --output_format json {} {} {} {}".format(
            input_dir,
            models[lang]["dictionary"],
            models[lang]["acoustic_model"],
            job.get_job_dir() + "/outputs",
        ),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # Check if subprocess ran successfully
    if pipe.returncode != 0:
        end = time.time()
        print("Error running mfa align: " + pipe.stderr.decode("utf-8"))
        return returnObj.error(
            msg="Error running mfa align: " + pipe.stderr.decode("utf-8"),
            code=500,
            data={
                "timeTaken": end - start,
                "job_id": job.get_job_id(),
            },
        )
    else:
        end = time.time()
        print("mfa align ran successfully, printing output: ")
        print(pipe.stdout.decode("utf-8"))
        return returnObj.success(
            msg="mfa align ran successfully",
            code=200,
            data={
                "timeTaken": end - start,
                "job_id": job.get_job_id(),
            },
        )


def converter(output_dir, json_filename, job: Job):
    # Implement covnerter like ../../src/mfa2gentle.py
    try:
        with open(output_dir + "/" + json_filename, "rb") as f:
            mfa_data = json.load(f)
            # MFA phones and words
            mfa_phones = mfa_data['tiers']['phones']['entries']
            mfa_words = mfa_data['tiers']['words']['entries']
            gwords =""

            # Get word from mfa
            words = [] # Maps to phones in gentle_out.json for a particular word. Eg. Array will contain all phones for word "this".
            
            for word_info in mfa_words:
                mfa_word_start = word_info[0]
                mfa_word_end = word_info[1]
                mfa_word = word_info[2]
                gwords += (mfa_word + " ").upper()

                # print("Word: " + mfa_word + " Start: " + str(mfa_word_start) + " End: " + str(mfa_word_end))

                gentle_word_set = {
                    "alignedWord": mfa_word,
                    "start": mfa_word_start,
                    "end": mfa_word_end,
                    "phones": [],
                    "word": mfa_word.upper(),
                }

                # Get phones from mfa for each word
                start_index = 0
                end_index = 0
                phones_for_word = []

                for i in range(len(mfa_phones)):
                    # print("Finding phones for word: ", mfa_word)
                    phone_set_start = mfa_word_start
                    phone_set_end = mfa_word_end
                    phone_info = mfa_phones[i]
                    if(phone_info[0] == phone_set_start):
                        # print("Found starting phone of word: ", mfa_word)
                        # Modify phone according to gentle_out.json
                        phone = {
                            'phone': phone_info[2],
                            'duration': phone_info[1] - phone_info[0],
                            'mfa_index': i,
                        }
                        start_index = i
                        # print(phone)
                        # phone_set.append(phone)
                        phones_for_word.append(phone)
                        continue
                    elif(phone_info[1] == phone_set_end):
                        # print("Found ending phone of word: ", mfa_word)
                        # Modify phone according to gentle_out.json
                        phone = {
                            'phone': phone_info[2],
                            'duration': phone_info[1] - phone_info[0],
                            'mfa_index': i,
                        }
                        end_index = i
                        # print(phone)
                        # phone_set.append(phone)
                        phones_for_word.append(phone)
                        break
                    # NOTE: Need index while looping to retrieve the phones between the start and end phones.
                    # Then set the iterator to the index of the last(end) phone in the set and break

                # Retrieve phones between start and end phones
                # print("Start and end phones phones for word: ", mfa_word, " : ", phones_for_word)
            
                if(len(phones_for_word) > 1):
                    for i in range(start_index+1, end_index):
                        # print("Retrieving phones between start index -", start_index," and end index -" , end_index,  "for word:" , mfa_word)
                        phone_info = mfa_phones[i]
                        phone = {
                            'phone': phone_info[2],
                            'duration': phone_info[1] - phone_info[0],
                            'mfa_index': i,
                        }
                        phones_for_word.insert(i, phone)
                    phones_for_word.sort(key=lambda x: x['mfa_index'])
                
                # print("Phones for word ", mfa_word, " : ", phones_for_word)
                gentle_word_set['phones'] = phones_for_word
                words.append(gentle_word_set)
            
            for word_set in words:
                # Add case key to phones
                word_set['case'] = 'success'

                for phone in word_set['phones']:
                # Fix duration decimals
                    phone['duration'] = round(phone['duration'], 5)
                # Remove mfa_index from phones
                    phone.pop('mfa_index', None)
            
            dict = {
                'transcript': gwords,
                'words': words,
            }

            dict['transcript'] = dict['transcript'].strip()
            mfa2gentle = json.dumps(dict, indent=4)

            # Add below code to try block
            try:
                # Write to file
                with open(output_dir + "/mfa_converted.json", "w") as f:
                    f.write(mfa2gentle)
                    # print("Wrote converted.json to " + output_dir + "/converted.json")
                    return returnObj.success(
                        msg="Wrote converted.json to " + output_dir + "/mfa_converted.json",
                        code=200,
                        data= {
                            "job_id": job.get_job_id(),
                        }
                    )
            except Exception as e:
                return returnObj.error(
                    msg="Error writing converted.json file: " + str(e),
                    code=500,
                    data= {
                        "job_id": job.get_job_id(),
                    }
                )

    except Exception as e:
        return returnObj.error(
            msg="Error opening mfa json file: " + str(e),
            code=500,
            data= {
                "job_id": job.get_job_id(),
            }
        )
