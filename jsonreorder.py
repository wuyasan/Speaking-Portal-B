import json
import pathlib


localpath = pathlib.Path(__file__).parent.resolve().parent.resolve()
f = open(str(localpath)+"/data/text/MFA.json", "r+")
data = json.loads(f.read())

f = open(str(localpath)+"/data/text/test.json", "r+")
target = json.loads(f.read())
ptr = 0
MFAwords = data['tiers']['words']['entries'] #grab words and entries 
MFAphones = data['tiers']['phones']['entries'] #grab phonemes and entries
#Gphones = target['words']['phones']

ptr = 0
for i in MFAwords:
    target['words'][ptr]['alignedWord'] = MFAwords[ptr][2]   #position of word in MFA JSON set to alignedWord in Gentle format
    target['words'][ptr]['end'] = MFAwords[ptr][1]   # position of end timestamp
    target['words'][ptr]['start'] = MFAwords[ptr][0]   # position of start timestamp
    target['words'][ptr]['word'] = MFAwords[ptr][2].upper() #set word to word
    idx = 0
    #for x in MFAphones[ptr]:   #inner loop to see how many phonemes per word, this loops 3x but should loop for amnt of phonemes in the given word
        #print(target['words'][ptr]['phones'][idx]['duration'])    #this line is duration position, set this equal to next line
        #print(MFAphones[idx][1] - MFAphones[idx][0]) #disparity    #this line calculates duration from start and finish
        #idx += 1                                                   #this loop runs out of bounds, need a better loop condition
    ptr += 1

print("\n")
#print(target['words'][0]['phones'][2]['duration']) # test to see if output is right
#print(MFAphones[2][1] - MFAphones[2][0])  #more tests
f.close()
