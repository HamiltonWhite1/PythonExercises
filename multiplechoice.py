# A teacher is looking for a program that checks student answers versus the correct answers.
    # the program asks for how many questions are on the test.
    # Then the program asks for the student answers
    # Then the program asks for the correct answers from the teacher
    # The program then checks the student answers against the correct answers, input by the teacher

NUMBER_OF_QUESTIONS = int(input("How many questions are on the test?: ")) #this asks the user how many questions are on the test
student_answers = [] #this is an empty list for student answers that is appended throughout the student loop
teacher_answers = [] #this is an empty list for the correct answers appended throughout the teacher loop

correct_answers = 0

for lines in range(NUMBER_OF_QUESTIONS): #this code runs a for loop for the number of questions on the test
    right_answer = input("Teacher, what is the correct answer to these questions?: ") #this code takes the correct answers from the teacher for each question on the test
    teacher_answers.append(right_answer) #this code appends each correct answer, in order, for the test, into the teacher_answers lists

for lines in range(NUMBER_OF_QUESTIONS): #this code runs a for loop for the number of questions on the test
    student_choice = input("Student, what were your answers for these questions?: ") #this code takes the student choice for answers for each question on the test
    student_answers.append(student_choice) #this code appends each student answer, in order, for each question on the test

for right_answer, guess_answer in zip(teacher_answers, student_answers): #this code 
    print((right_answer, guess_answer))
    if right_answer == guess_answer:
        correct_answers += 1


print(correct_answers)

# for i,k in zip([1,2,3], ['A', 'B','C']): 
#     print((i,k))