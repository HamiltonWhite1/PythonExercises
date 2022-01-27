###Counts the number of X's and O's in a string, and returns True if x_count and o_count are equal to one another

def xo(s):
    x_count = 0
    o_count= 0
    for i in s:
        if i == "x" or i == "X":
            x_count += 1
        if i == "o" or i == "O":
            o_count += 1
    
    if x_count == o_count:
        return True
    else:
        return False

xo("xoxoxo")