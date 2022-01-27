s='hello'
new=[]

b="this is my new string"

def wave(people):
    for i, val in enumerate(people[:]):
        up=people[i].upper()
        c=people[:i] + up + people[i+1:]
        new.append(c)
    return new
wave(b)