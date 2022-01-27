vowel_code = {
    "a": 1,
    "e": 2,
    "i": 3,
    "o": 4,
    "u": 5
}

def encode(st):
    for i in st:
        if i in vowel_code.keys():
            i = vowel_code.values()
    print(st)
encode("this is my test string")
    
def decode(st):
    return
decode("th3s 3s my t2st st3ng")