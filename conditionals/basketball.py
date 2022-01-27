
# banana_three = int(input('How many three-pointers did the bananas make: '))
# banana_two = int(input('How many two-pointers did the bananas make: '))
# banana_free_throw = int(input('How many free throws did bananas make: '))
# apple_three = int(input('How many three-pointers did the apples make: '))
# apple_two = int(input('How many two-pointers did the apples make: '))
# apple_free_throw = int(input('How many free throws did the apples make: '))

# BANANAS_SCORE = (banana_three * 3) + (banana_two * 2) + (banana_free_throw)
# APPLES_SCORE = (apple_three * 3) + (apple_two * 2) + (apple_free_throw)

# if BANANAS_SCORE > APPLES_SCORE:
#     print('The Bananas won')
# elif BANANAS_SCORE == APPLES_SCORE:
#     print('The Apples and Bananas tied')
# else:
#     print('The Apples won')

def get_basketball_outcome():
    banana_3, banana_2, banana_1 = input('How many three-pointers, two-pointers, and free throws did banana team make? (three, two, free): ').split()
    banana_outcome = (int(banana_3) * 3) + (int(banana_2) * 2) + (int(banana_1) * 1)
    apple_3, apple_2, apple_1 = input('How many three-pointers, two-pointers, and free throws did apple team make? (three, two, free): ').split()
    apple_outcome = (int(apple_3) * 3) + (int(apple_2) * 2) + (int(apple_1) * 1)
    if banana_outcome > apple_outcome:
        print('Bananas win')
    elif banana_outcome == apple_outcome:
        print('Bananas and Apples tie')
    else:
        print('Apples win')
get_basketball_outcome()

# def peanuts():
#     peanuts, walnuts = input('How many peanuts do you have? How many walnuts do you have?').split()
#     nuts = int(peanuts) + int(walnuts)
#     print(nuts)
# peanuts()

