import json
import pathlib
localpath = pathlib.Path(__file__).parent.resolve().parent.resolve()
with open(str(localpath) + "/data/text/MFA.json") as f:
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
    #print(mfa_word_start, mfa_word_end, mfa_word)
    gentle_word_set = {
        'alignedWord': mfa_word,
        'start': mfa_word_start,
        'end': mfa_word_end,
        'word': mfa_word.upper(),
        'phones': []
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
    
    #print("Phones for word ", mfa_word, " : ", phones_for_word)
    gentle_word_set['phones'] = phones_for_word
    words.append(gentle_word_set)


for word_set in words:
    # TODO: Add case key to phones
    word_set['case'] = 'success'

    for phone in word_set['phones']:
    # TODO: Fix duration decimals
        phone['duration'] = round(phone['duration'], 5)
    # TODO: Remove mfa_index from phones
        phone.pop('mfa_index', None)

dict = {
    'transcript': gwords,
    'words': words,
}

mfa2gentle = json.dumps(dict)

# Write to file
with open(str(localpath) + "/data/text/mfa2gentle.json", 'w') as f:
    f.write(mfa2gentle)

