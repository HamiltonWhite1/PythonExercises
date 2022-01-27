
test_list = [1,2,"a","b"]
def filter_list(l):
    stringless_list = []
    for i in l:
        if i != str(i):
            stringless_list.append(i)
    return stringless_list
filter_list(test_list)
