test_data = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
def data_reverse(data):
    reversed_list = []
    byte_list = []
    for i in data:
        byte_list.append(i)
        if len(byte_list) == 8:
            print(byte_list)
            reversed_list.insert(0, byte_list.reverse())
            byte_list = []
    print(reversed_list)
data_reverse(test_data)

