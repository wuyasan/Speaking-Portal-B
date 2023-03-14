
OG_PHONE_MOUTH_MAP = [["aa", "a"], ["ae", "a"], ["ah", "a"], ["ao", "a"], ["aw", "au"],
                ["ay", "ay"], ["b", "m"], ["ch", "t"], ["d", "t"], ["dh", "t"],
                ["eh", "a"], ["er", "u"], ["ey", "ay"], ["f", "f"], ["g", "t"],
                ["hh", "y"], ["ih", "a"], ["iy", "ay"], ["jh", "t"], ["k", "t"],
                ["l", "y"], ["m", "m"], ["n", "t"], ["ng", "t"], ["ow", "au"],
                ["oy", "ua"], ["p", "m"], ["r", "u"], ["s", "t"], ["sh", "t"],
                ["t", "t"], ["th", "t"], ["uh", "u"], ["uw", "u"], ["v", "f"],
                ["w", "u"], ["y", "y"], ["z", "t"], ["zh", "t"],
                ["oov", "m"]]

ENGLISH_US_ARPA_PHONES = ['AA0', 'AA1', 'AA2', 'AE0', 'AE1', 'AE2', 'AH0', 'AH1', 'AH2', 'AO0', 'AO1', 'AO2', 'AW0', 'AW1', 'AW2', 'AY0', 'AY1', 'AY2', 'B', 'CH', 'D', 'DH', 'EH0', 'EH1', 'EH2', 'ER0', 'ER1', 'ER2', 'EY0', 'EY1', 'EY2', 'F', 'G', 'HH', 'IH0', 'IH1', 'IH2', 'IY0', 'IY1', 'IY2', 'JH', 'K', 'L', 'M', 'N', 'NG', 'OW0', 'OW1', 'OW2', 'OY0', 'OY1', 'OY2', 'P', 'R', 'S', 'SH', 'T', 'TH', 'UH0', 'UH1', 'UH2', 'UW0', 'UW1', 'UW2', 'V', 'W', 'Y', 'Z', 'ZH']
"""
Map of English US ARPA phones to mouth shapes
key: phone (lowercase)
value: mouth shape (lowercase)
"""
ENGLISH_US_ARPA_PHONE_MOUTHS = {'aa': 'a', 'ae': 'a', 'ah': 'a', 'ao': 'a', 'aw': 'au', 'ay': 'ay', 'b': 'm', 'ch': 't', 'd': 't', 'dh': 't', 'eh': 'a', 'er': 'u', 'ey': 'ay', 'f': 'f', 'g': 't', 'hh': 'y', 'ih': 'a', 'iy': 'ay', 'jh': 't',
             'k': 't', 'l': 'y', 'm': 'm', 'n': 't', 'ng': 't', 'ow': 'au', 'oy': 'ua', 'p': 'm', 'r': 'u', 's': 't', 'sh': 't', 't': 't', 'th': 't', 'uh': 'u', 'uw': 'u', 'v': 'f', 'w': 'u', 'y': 'y', 'z': 't', 'zh': 't', 'oov': 'm'}
    

# TODO: Add phone to mouth maps for other languages
JAPANESE_PHONES = ["a", "aː", "b", "bʲ", "bː", "c", "cː", "d", "dz", "dzː", "dʑ", "dʑː", "dʲ", "dː", "e", "eː", "h", "hː", "i", "iː", "i̥", "j", "k", "kː", "m", "mʲ", "mʲː", "mː", "n", "nː", "o", "oː", "p", "pʲ", "pʲː", "pː", "s", "sː", "t", "ts", "tsː", "tɕ", "tɕː", "tʲ", "tʲː", "tː", "v", "vʲ", "w", "z", "ç", "ŋ", "ɕ", "ɕː", "ɟ", "ɟː", "ɡ", "ɡː", "ɨ", "ɨː", "ɨ̥", "ɯ", "ɯː", "ɯ̥", "ɰ̃", "ɲ", "ɲː", "ɴ", "ɴː", "ɸ", "ɸʲ", "ɸʲː", "ɸː", "ɾ", "ɾʲ", "ʑ", "ʔ"]
"""
Map of Japanese phones to mouth shapes
key: phone (lowercase)
value: mouth shape (lowercase)
"""
JAPANESE_PHONES_MOUTHS = {'a': 'a', 'aː': 'a', 'b': 'm', 'bʲ': 'm', 'bː': 'm', 'c': 't', 'cː': 't', 'd': 't', 'dz': 't', 'dzː':'t', 'dʑ':'t', 'dʑː':'t', 'dʲ':'t', 'dː':'t', 'e':'a', 'eː':'a', 'h':'y', 'hː':'y', 'i':'ay', 'iː':'ay', 'i̥':'ay', 'j':'t', 'k':'t', 'kː':'t', 'm':'m', 'mʲ':'m', 'mʲː':'m', 'mː':'m', 'n':'m', 'nː':'m', 'o':'au', 'oː':'au', 'p':'m', 'pʲ':'m', 'pʲː':'m', 'pː':'m', 's':'t', 'sː':'t', 't':'t', 'ts':'t', 'tsː':'t', 'tɕ':'t', 'tɕː':'t', 'tʲ':'t', 'tʲː':'t', 'tː':'t', 'v':'u', 'vʲ':'u', 'w':'u', 'z':'t', 'ç':'y', 'ŋ':'t', 'ɕ':'f', 'ɕː':'f', 'ɟ':'t', 'ɟː':'t', 'ɡ':'t', 'ɡː':'t', 'ɨ':'u', 'ɨː':'u', 'ɨ̥':'u', 'ɯ':'u', 'ɯː':'u', 'ɯ̥':'u', 'ɰ̃':'t', 'ɲ':'t', 'ɲː':'t', 'ɴ':'n', 'ɴː':'n', 'ɸ':'f', 'ɸʲ': 'f', 'ɸʲː':'f', 'ɸː':'f', 'ɾ':'y', 'ɾʲ':'y', 'ʑ':'t', 'ʔ':'u'}
"""
@params: lang - the language to get the phone to mouth map for
@return: dict - phone: mouth
Returns the phone to mouth map for the given language
Default is English
"""
def getMouthDict(lang):
    if lang == None or lang == "":
        return ENGLISH_US_ARPA_PHONE_MOUTHS

    if lang == "ENGLISH":
        return ENGLISH_US_ARPA_PHONE_MOUTHS

    if lang == "JAPANESE":
        return JAPANESE_PHONES_MOUTHS