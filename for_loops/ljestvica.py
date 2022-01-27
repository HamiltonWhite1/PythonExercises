# Take a line of input that contains from 5 to 100 characters from the sest [A, B, C, D, E, F, G, |]

# if the line of input contains more C, F and G notes, the line is most likely written in C-Major.
    # and therefor the output is C-dur

# If the line of input contains A, D and E notes, the line is most likely written in A-Minor.
    # and therefor the output is A-mol

# Create a line of input for the musical notes

musical_notes = input('Please input your composition. Remember to divide your bars with the "|" character: ').upper()
print(musical_notes) #musical_notes stores the bars of music input by user. This is the only input in the program

# A_MINOR_NOTES AND C_MAJOR_NOTES are variables starting at 0 and will be incremented throughout the for loop by 1 as each type of note is iterated over
A_MINOR_NOTES = 0 
C_MAJOR_NOTES = 0

# sample input1
'AEB|C'

# sample input2
'CD|EC|CD|EC|EF|G|EF|G|GAGF|EC|GAGF|EC|CG|C|CG|C'


for i in range(len(musical_notes)):
    character = musical_notes[i]
    if i == 0:
        if character == 'A' or character == 'D' or character == 'E': 
            A_MINOR_NOTES += 1 
        elif character == 'C' or character == 'F' or character == 'G': 
            C_MAJOR_NOTES += 1 

    if character == '|':
        next_note = musical_notes[i + 1]
        if next_note == 'A' or next_note == 'D' or next_note == 'E': 
            A_MINOR_NOTES += 1 
        elif next_note == 'C' or next_note == 'F' or next_note == 'G': 
            C_MAJOR_NOTES += 1 

if A_MINOR_NOTES > C_MAJOR_NOTES: #this code is successful based on the print statements below testing correctly for the desired behavior
        print('A-mol')
        print(f"There are {A_MINOR_NOTES} A-minor notes")
        print(f"There are {C_MAJOR_NOTES} C-major notes")
elif A_MINOR_NOTES < C_MAJOR_NOTES: #this code is successful based on the print statements below testing correctly for the desired behavior
        print('C-dur')
        print(f"There are {A_MINOR_NOTES} A-minor notes")
        print(f"There are {C_MAJOR_NOTES} C-major notes")

####If the number of main A_MINOR_NOTES is equal to C_MAJOR_NOTES, write code that determines whether or not the scale is A-minor or C-major
####Based on the last main note (A or C) in the composition
if A_MINOR_NOTES == C_MAJOR_NOTES: ###this line of code checks if A_MINOR_NOTES variable and C_MAJOR_NOTES variable are equal. If true:
    if musical_notes[-1] == 'A': ##this line of code checks if the value at the last index of musical_notes is 'A'. If true:
            print('A-mol') #print that the scale is A-minor
            print('The last main note was "A"')#and also print the reason why per the assignment instructions
    elif musical_notes[-1] == 'C':##this line of code checks if the value of the last index of musical_notes is 'C'. If true:
            print('C-dur')#print that the scale is C-major
            print('The last main note was "C"')#and also print the reason why per the assignment instructions



 