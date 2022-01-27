###Function that returns the length of the shortest word in a string
def find_short(s):
    s_split = s.split()
    s_split.sort(key=len)
    return s_split[0]
find_short("This is my test string")