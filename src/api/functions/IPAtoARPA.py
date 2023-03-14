import json
import pathlib

_arpabet2ipa = {
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


localpath = pathlib.Path(__file__).parent.resolve().parent.resolve().parent.resolve().parent.resolve()
JSONpath = str(localpath) + "/data/text/MFA.json"
with open(JSONpath, 'r', encoding = 'utf-8') as f:
    data = json.load(f)
    entries = data['tiers']['phones']['entries']
    for x in entries:
        phones = x[2]
        for y in phones:
            print(_arpabet2ipa.get(y))
        

with open(JSONpath, 'w', encoding = 'utf-8') as f:
    json.dump(data,f,ensure_ascii=False)
   

