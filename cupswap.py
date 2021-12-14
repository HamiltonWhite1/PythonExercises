# Convert the below code into a function


# def cup_swap():
#     ball_location = 1
#     swaps = input("Please type 'A', 'B', or 'C' to play the game and move the cups: " )
#     if swaps.upper() == ['A', 'B', 'C'] and ball_location == 1:
#         ball_location = [1, 2, 3]
#         return ball_location
# cup_swap()


# range(1, 20)
# range(0, 20)
# range(20)

from random import choice

def swap_cups():
    ball_location = 1
    swaps = int(input("How many times would you like the cups to move?: "))
    swap_types = ['A', 'B', 'C']

    for swap_count in range(swaps):
        swap_type = choice(swap_types)
        if swap_type == 'A' and ball_location == 1:
            ball_location = 2
            print('Ball is in position {}'.format(ball_location))
        elif swap_type == 'B' and ball_location == 1:
            ball_location = 1
            print('Ball is in position {}'.format(ball_location))
        elif swap_type == 'C' and ball_location == 1:
            ball_location = 3
            print('Ball is in position {}'.format(ball_location))
        elif swap_type == 'A' and ball_location == 2:
            ball_location = 1
            print('Ball is in position {}'.format(ball_location))
        elif swap_type == 'B' and ball_location == 2:
            ball_location = 3
            print('Ball is in position {}'.format(ball_location))
        elif swap_type == 'C' and ball_location == 2:
            ball_location = 2
            print('Ball is in position {}'.format(ball_location))
        elif swap_type == 'A' and ball_location == 3:
            ball_location = 3
            print('Ball is in position {}'.format(ball_location))
        elif swap_type == 'B' and ball_location == 3:
            ball_location = 2
            print('Ball is in position {}'.format(ball_location))
        elif swap_type == 'C' and ball_location == 3:
            ball_location = 1
            print('Ball is in position {}'.format(ball_location))

swap_cups()

#  A input is swapping the left cup with the middle cup
#  B input is swapping the middle and right cups
#  C input is swapping the left and right cups
# Pos1 = ball is at the left
# Pos2 = ball in the middle
# Pos3 = ball is at the right
