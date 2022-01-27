small_arr = [34, 15, 88, 2]

def find_smallest_int(arr):
    arr.sort()
    return arr[0]
find_smallest_int(small_arr)