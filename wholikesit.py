empty_names =[]
list_of_names = ["Jason", "John"]

def likes(names):
    length = len(names) - 2
    if len(names) == 0:
        return "no one likes this"
    if len(names) == 1:
        for i in names:
            return f"{i} likes this"
    if len(names) == 2:
        for i in names:
            return f"{i} and {names[1]} like this"
    if len(names) == 3:
        for i in names:
            return f"{i}, {names[1]} and {names[2]} like this"
    if len(names) >= 3:
        for i in names:
            return f"{i}, {names[1]} and {length} others like this"

print(likes(empty_names))