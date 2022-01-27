test_string = "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"

def sum_of_integers_in_string(s):
    nums = '1234567890'
    sum = 0
    for i in s:
        if i in nums:
            i = int(i)
            sum += i
    return sum
sum_of_integers_in_string(test_string)
