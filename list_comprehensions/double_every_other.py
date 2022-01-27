###List comprehension function that returns a list with every other number multiplied by 2.

num_lst = [1,19,6,2,12,-3]

def double_every_other(lst):
    lst[1::2] = [num*2 for num in lst[1::2]]
    return lst
double_every_other(num_lst)