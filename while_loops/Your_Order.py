test_string = "is2 Thi1s T4est 3a"

def order(sentence):
    sorted_str = ""
    splits = sentence.split()
    while len(sorted_str) < len(sentence):
        for split in splits:
            for i in split:
                if i == '1':
                    sorted_str += split + " "
    print(sorted_str)
order(test_string)
