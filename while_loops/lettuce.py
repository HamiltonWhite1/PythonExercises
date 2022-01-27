

import random

MAX_GUESSES = 5
NUMBER_OF_CHARACTERS = 3

def main():

    print('''This is a game where I will generate a list of {} letters. There will be no repeated letters in each list. Try to guess the list.
    When I say:         That means:
    Bacon:              One letter is correct, but it is in the wrong position
    Lettuce:            One letter is correct, and in the right position
    Tomatoes:           No letters are correct      
    '''.format(NUMBER_OF_CHARACTERS))


    while True:
        random_letters = get_random_letters()
        print("I have thought of a list")
        print("You have {} guesses to get the list correct".format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUMBER_OF_CHARACTERS or not guess.isdecimal():
                print("Guess #{}: ".format(num_guesses))
                guess = input('> ')
            
            clues = get_clues(guess, random_letters)
            print(clues)
            num_guesses += 1

            if guess == random_letters:
                break
            if num_guesses > MAX_GUESSES:
                print("Sorry, you ran out of guesses")
                print("The answer was {}".format(random_letters))

        print("Do you want to play again? (yes/no)")
        if not input('> ').lower().startswith('y'):
            break
        print("Thanks for playing!")

def get_random_letters():
    letters = list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(letters)
    
    random_letters = ' '
    for i in range(NUMBER_OF_CHARACTERS):
        random_letters += str(letters[i])
    return random_letters

def get_clues(guess, random_letters):
    if guess == random_letters:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == random_letters[i]:
            clues.append('Lettuce')
        elif guess[i] in random_letters:
            clues.append('Bacon')
        if len(clues) == 0:
            return 'Tomatoes'
        else:
            clues.sort()
            return ' '.join(clues)

if __name__ == '__main__':
    main()


