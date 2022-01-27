# Create a program that checks if a string of characters that contains the subword 'HONI' as a block. 
    # For example, if the string is "asdsahasdaoasdanasdai", the presence of the 'h' character, the 'o' character, the 'n' character, and the 'i' character make a 'HONI' block

# Create a user input statement to receive the string

user_string = input("Please input a list of characters of your choosing: ").upper()
# create a variable to store the number of HONI blocks in a string
HONI_BLOCKS = 0
# create conditions to check for the presence of the "HONI" block characters
for char in user_string:
    if char.upper() == "H":
        num_of_H = user_string.count('H')
    elif char.upper() == "O":
        num_of_O = user_string.count('O')
    elif char.upper() == "N":
        num_of_N = user_string.count('N')
    elif char.upper() == "I":
        num_of_I = user_string.count('I')

if (num_of_H == num_of_O) == (num_of_N == num_of_I):
    HONI_BLOCKS = num_of_H
# Output the total of HONI blocks in the string
print(f'There are: {HONI_BLOCKS} HONI blocks')