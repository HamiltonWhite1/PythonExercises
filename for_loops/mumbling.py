test_string = "abcd"


def accum(s):
    return_string = ''
    for i in s:
        return_string = return_string + i.upper()
        print(return_string)
    print(return_string)
accum(test_string)

