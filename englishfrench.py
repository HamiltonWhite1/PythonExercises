# Create a program that guesses whether or not input text is French or English
    # if the input contains more 't' or "T" characters, guess English
    # if the input contains more 's' or "S" characters, guess French
    # if the number of 't' and "T" characters is the same as number of 's' and "S" characters, guess French

# The below explains the function of the program
print('''This is a Natural Language Processing program that guesses if a series of input lines are English or French.
Please input three lines, in either English or French, and the program will guess which lanuage you have input based on a few parameters.''')

# storing user input
first_line = input('Please input your first line of English or French: ')
second_line = input('Please input your second line of Eglish or French (it should be the first language as the first line):  ')
third_line = input('Please input your third line of English or French(same as first line): ')

# the below variables are stored with empty strings, and will be modified during each for loop iteration as applicable
english_one = 0
english_two = 0
english_three = 0
ENGLISH_SUM = english_one + english_two + english_three

french_one = 0
french_two = 0
french_three = 0
FRENCH_SUM = french_one + french_two + french_three

#this function utilizes for loops and if statements to check the sum of 't', 'T' characters, and 's', 'S' characters.
def english_french(): 
    for char in first_line:
        if char == 't' or char == 'T':
            english_one = first_line.count('t') + first_line.count('T')
            print(f"there are {english_one} english one characters")
        elif char == 's' or char == 'S':
            french_one = first_line.count('s') + first_line.count('S')
            print(f" there are {french_one} french characters") 
    for char in second_line:
        if char == 't' or char == 'T':
            english_two = second_line.count('t') + second_line.count('T')
            print(f"there are {english_two} english characters")
        elif char == 's' or char == 'S':
            french_two = second_line.count('s') + second_line.count('S')
            print(f" there are {french_two} french characters")
    for char in third_line:
        if char == 't' or char == 'T':
            english_three = third_line.count('t') + third_line.count('T')
            print(f"there are {english_three} english characters")
            print(f"The sum of English characteres is {ENGLISH_SUM}")
        elif char == 's' or char == 'S':
            french_three = third_line.count('s') + third_line.count('S')
            print(f" there are {french_three} french characters")
            print(f"The sum of FRENCH characteres is {FRENCH_SUM}")

    #after evaluating the number of specific characters, these if and elif statements check the sum of English and French characters 
    #and print our desired results from the challenge instructions
english_french()

