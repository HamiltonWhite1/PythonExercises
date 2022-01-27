
# def digital_root(n):
#     recursive_list= []
#     rec_sum = 0
#     for i in str(n):
#         recursive_list.append(int(i))
#     for i in recursive_list:
#         rec_sum += i
    
# digital_root(597)

# def digital_root(n):
#     recursive_sum = 0
#     recursive_interval = 0
#     recursive_final = 0
#     if len(str(n)) > 1:
#         for i in str(n):
#             recursive_interval += int(i)
#         if len(str(recursive_interval)) == 1:
#             recursive_sum = recursive_interval
#     if len(str(recursive_interval)) > 1:
#         for i in str(recursive_interval):
#             recursive_sum += int(i)
#         if len(str(recursive_sum)) > 1:
#             for i in str(recursive_interval):
#                 recursive_final =+ int(i)
#         recursive_sum = recursive_final
            
#     print(recursive_sum)
    
# digital_root(11)

def digital_root(n):
    sum = 0
    int_sum = 0
    for i in str(n):
        sum += int(i)
        if len(str(sum)) == 2:
            for i in str(sum):
                int_sum += int(i)
            sum = int(sum)

    print(int_sum)
digital_root(4323434)

# def digital_root(n):
#     recursive_sum = 0
#     while len(str(n)) > 1:
#         for i in str(n):
#             recursive_sum += int(i)
#         if len(str(recursive_sum)) == 1:
#             n = recursive_sum
#         else:
#             for i in str(recursive_sum):
#                 n += int(i)
    
#     print(n)


# digital_root(1123232)