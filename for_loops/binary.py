###Function that returns how many binary bits (1's) are in an integer

def count_bits(n):
    bit_count = 0
    binary = format(n, "b")
    for i in str(binary):
        if i == "1":
            bit_count += 1
    return bit_count
count_bits(100)
