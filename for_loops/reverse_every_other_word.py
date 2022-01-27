###Function that returns a string with every other word reversed

test_string = "This is my test string"

def descending_order(string):
    string = string.split()
    test_list = []
    for i in string:
        if i in string[1::2]:
            i = i[::-1]
            test_list.append(i)
        else:
            test_list.append(i)
    test_list = ' '.join(test_list)
    return test_list
descending_order(test_string)