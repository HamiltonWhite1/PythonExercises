phone_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def create_phone_number(n):
    area_code = ""
    second_three = ""
    last_four = ''
    for num in n[:3]:
        num = str(num)
        area_code = area_code + num
    for num in n[4:7]:
        num = str(num)
        second_three = second_three + num
    for num in n[7:]:
        num = str(num)
        last_four = last_four + num
    phone_num = f"({area_code})" + " " + f"{second_three}" + "-" + f"{last_four}"
    print(area_code)
    print(second_three)
    print(last_four)
    print(phone_num)
create_phone_number(phone_num)