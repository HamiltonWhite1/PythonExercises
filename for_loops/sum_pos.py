
test_array = [1, -4, 7, 12]
def positive_sum(arr):
    arr_sum = 0
    for i in arr:
        if i >= 0:
            arr_sum += i
    return arr_sum
positive_sum(test_array)