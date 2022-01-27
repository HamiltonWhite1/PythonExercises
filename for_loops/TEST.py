# The below explains the function of the program
print('''This is a Natural Language Processing program that guesses if a series of input lines are English or French.
Please input three lines, in either English or French, and the program will guess which lanuage you have input based on a few parameters.''')

# storing user input
first_line = input('Please input your first line of English or French: ')
second_line = input('Please input your second line of Eglish or French (it should be the first language as the first line):  ')
third_line = input('Please input your third line of English or French(same as first line): ')

def english_french(line): 
    # we initialize the counts of characters to 0 
    english_count = 0 # this
    french_count = 0 # this
    
    # increments sum of english or french characters if we see one of the characters from those languages
    # line ssTS
    for char in line:
        if char == 't' or char == 'T':
            english_count += 1
            print(f"there are {english_count} english characters")
        if char == 's' or char =='S':
            french_count += 1
            print(f"there are {french_count} french characters")
    
    # return a tuple of english_count and french_count
    return (english_count, french_count)
 
ENGLISH_SUM = 0
FRENCH_SUM = 0
for line in [first_line, second_line, third_line]: 
    english_count, french_count = english_french(line)
    ENGLISH_SUM += english_count
    FRENCH_SUM += french_count
    
if ENGLISH_SUM > FRENCH_SUM: 
      print('Is the excerpt you submitted in English?')
elif ENGLISH_SUM < FRENCH_SUM:
    print('Is the excerpt you submitted in French?')