# password must be between 8 and 12 characters long
password_instructions= print('''Please input a password that is between 8 and 12 characters long. It must have at least three lowercase characters, 
two uppercase characters, and one digit''')
verified_password = input('Please input your new password: ')
# password must contain at least three lowercase, two uppercase, and at least one digit
# verify the above conditions

proper_capital_count = sum(1 for c in verified_password if c.isupper())
proper_lower_count = sum(1 for l in verified_password if l.islower())
proper_digit_count = sum(1 for d in verified_password if d.isdigit())

if len(verified_password) >= 8 and len(verified_password) <= 12: #this check if the length of the user input for the password is >= 8 and <=12
    print("Okay, good, your password is long enough.")
else:
    print('Please try again. The password must be between 8 and 12 characters.')
if proper_capital_count >= 2:  #this checks if variable proper_capital_count stores the minimum or greater sum of capital characters
    print('Okay, good, you have the proper capitalization.')
else:
        print('There are not enough capital letters in this password.')
if proper_lower_count >= 3: #this checks if variable proper_lower_count stores the minimum num of lowercase characters, or a greater sum of lowercase characters.
    print('Okay, you have he correct amount of lowercase letters.')
else:
    print('You do not have enough lowercase letters in this password.')
if proper_digit_count >= 1: #checks if there is at least one integer in the password
    print('Awesome, you have the correct number of digits in this password.')
else:
    print('It looks like you need at least 1 number in this password')

# the below checks that all of the above conditional statements evaluate as true, and prints that the password is correct in total
if len(verified_password) >= 8 and len(verified_password) <= 12 and proper_capital_count >= 2 and proper_lower_count >= 3 and proper_digit_count >= 1:
    print('Congratulations, you have set your new password!')