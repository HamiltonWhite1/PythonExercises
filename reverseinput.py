def reverse_name():
    name = input("Please tell me your name, and I will reverse it: ")
    return name[::-1]

name = reverse_name()
print(name)