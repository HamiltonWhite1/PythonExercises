test_s = [1, 1, 1]
test_n = 10

def tribonacci(signature, n):
    trib_seq = []
    new_num = 0
    num_slice = 0
    if n > 0:
        if n == 1:
            trib_seq.append(signature[0])
        elif n == 2:
            trib_seq.append(signature[0])
            trib_seq.append(signature[1])
        elif n > 1:
            for i in signature: 
                trib_seq.append(i)
            while len(trib_seq) < n:
                for num in trib_seq[num_slice:]:
                    new_num += num
                trib_seq.append(new_num)
                new_num = 0
                num_slice += 1
        return trib_seq
    else:
        return trib_seq

tribonacci(test_s, test_n)

