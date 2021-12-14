
# digit_one = int(input('Please enter the first digit of the phone number: '))
# digit_two = int(input('Please enter the second digit of the phone number: '))
# digit_three = int(input('Please enter the third digit of the phone number: '))
# digit_four = int(input('Please enter the fourth digit of the phone number: '))

# if digit_one in [8,9] or digit_four in [8,9] and digit_two == digit_three:
#     print('Ignore the phone, this is a telemarketer.')
# else:
#     print('This is not a telemarketer, you can answer the phone.')

digit_one = int(input('Please enter the first digit in the number: '))
digit_two = int(input('Please enter the second digit in the number: '))
digit_three = int(input('Please enter the third digit in the number: '))
digit_four = int(input('Please enter the fourth digit in the number: '))

if ((digit_one == 8 or digit_one == 9) and (digit_four == 8 or digit_four == 9) and (digit_two == digit_three)):
    print('Ignore the phone, this is a telemarketer')
else:
    print('Answer the phone, this is not a telemarketer')
