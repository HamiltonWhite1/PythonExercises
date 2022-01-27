def solution(number):
    list_num = []
    sum_num = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            list_num.append(i)
    for i in list_num:
        sum_num += int(i)
    return sum_num
solution(10)