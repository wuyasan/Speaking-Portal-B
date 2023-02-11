import json

# Load data from gentle_out.json and mfa_out.json
with open('gentle_out.json') as f:
    gentle_data = json.load(f)
with open('mfa_out.json') as f:
    mfa_data = json.load(f)


# MFA phones and words
mfa_phones = mfa_data['tiers']['phones']['entries']
mfa_words = mfa_data['tiers']['words']['entries']

# Num of words in gentle and mfa
gentle_num_words = len(gentle_data['words'])
mfa_num_words = len(mfa_words)



# Check if the number of words are the same
if gentle_num_words == mfa_num_words:
    print('The number of words are the same', gentle_num_words, '==',  mfa_num_words)
else:
    print('The number of words are different', gentle_num_words, '!=',  mfa_num_words)
    exit(1)

# Get word from mfa
words = [] # Maps to phones in gentle_out.json for a particular word. Eg. Array will contain all phones for word "this".
for word_info in mfa_words:
    mfa_word_start = word_info[0]
    mfa_word_end = word_info[1]
    mfa_word = word_info[2]
    print(mfa_word_start, mfa_word_end, mfa_word)
    gentle_word_set = {
        'alignedWord': mfa_word,
        'start': mfa_word_start,
        'end': mfa_word_end,
        'word': mfa_word,
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
    elif(len(phones_for_word) == 1):
        print("Only one phone for word: ", mfa_word)
        # phone_set.append(phones_for_word[0])
    
    print("Phones for word ", mfa_word, " : ", phones_for_word)
    gentle_word_set['phones'] = phones_for_word
    words.append(gentle_word_set)

dict = {
    'transcript': "this is a test",
    'words': words,
}

mfa2gentle = json.dumps(dict)

# Write to file
with open('mfa2gentle.json', 'w') as f:
    f.write(mfa2gentle)



# Num of phones in gentle
# for i, phone_info in enumerate(phone_set):
#     print(i, phone_info)