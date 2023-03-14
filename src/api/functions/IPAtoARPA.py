import json
import pathlib
from jobQueue import Job
from returnObj import success, error
_ipa2arpabet = {
    'a':'AA',
    'ɑ':'AA',
    'a':'AE',
    'a':'AH',
    'ɛ̃':'AH',
    'ɔ':'AO',
    'o':'AW',
    'a':'AY',
    'ə':'AY',
    'e':'EH',
    'ɑ̃':'EH',
    'ɛ':'EH',
    'e':'ER',
    'e':'ER0',
    'a':'EY',
    'i':'IH',
    'i':'IH0',
    'i':'IY',
    'w':'OW',
    'ø':'OW',
    'œ':'OW',
    'ɔ̃':'OW',
    'o':'OY',
    'u':'UH',
    'u':'UW',
    'b':'B',
    'tʃ':'CH',
    'd':'D',
    'tʃ':'DH',
    'l':'EL',
    'm':'EM',
    'mʲ':'EM',
    'n':'EN',
    'f':'F',
    'ɡ':'G',
    'h':'HH',
    'dʒ':'JH',
    'k':'K',
    'ɟ':'K',
    'l':'L',
    'm':'M',
    'n':'N',
    'ɲ':'N',
    'ŋ':'NG',
    'p':'P',
    'k':'Q',
    'ʁ':'R',
    's':'S',
    'ʃ':'SH',
    't':'T',
    'ts':'T',
    'θ':'TH',
    'v':'V',
    'w':'W',
    'ʍ':'WH',
    'j':'Y',
    'ʎ':'Y',
    'ɥ':'Y',
    'z':'Z',
    'ʒ':'ZH'
}

def convert_IPA_to_ARPA(input_path, output_path, job: Job = None):
    try:
        with open(input_path, 'r') as f:
            data = json.load(f)
            entries = data['tiers']['phones']['entries']
            for i, x in enumerate(entries, start=0):
                print("Old entry: " + str(x))
                ipa_phone = x[2]
                arpa_phone = _ipa2arpabet.get(ipa_phone)
                print("Converting: " + str(ipa_phone) + " with length: " + str(len(ipa_phone)) + " to " + str(arpa_phone))
                # TODO: If none, either add relevant ARPA to dict for corresponding phone or replace with `spn` which is the default for unknown phones in MFA.
                if arpa_phone is None:
                    print("Got None for: " + str(ipa_phone) +  " , replacing with spn")
                    arpa_phone = "spn"
                x[2] = arpa_phone
                print("New entry: " + str(x))
                entries[i] = x
            data['tiers']['phones']['entries'] = entries

            converted_arpa_json = json.dumps(data, indent=4)
            
            with open(output_path, 'w', encoding = 'utf-8') as f:
                f.write(converted_arpa_json)
                print("Successfully converted IPA to ARPA")
                # return success("Successfully converted IPA to ARPA", code=200, job_id=job.get_job_id(), data={
                #     "converted_arpa_json": converted_arpa_json,
                # })
    except Exception as e:
        print("Error converting IPA to ARPA: " + str(e))
        # return error("Error converting IPA to ARPA: " + str(e), code=500, job_id=job.get_job_id())

localpath = pathlib.Path(__file__).parent.resolve().parent.resolve().parent.resolve().parent.resolve()
input_path = str(localpath) + "/data/text/MFA.json"
output_path = str(localpath) + "/data/text/MFA_ARPA.json"

convert_IPA_to_ARPA(input_path, output_path)

