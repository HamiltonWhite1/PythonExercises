number_of_cars = 10
yesterday_cars = '..CC..CC..'
today_cars = 'CCCCCCCCCC'
cars_parked = 0

# yesterday_cars[4] == today_cars[4]

for car in range(len(yesterday_cars)):

    if yesterday_cars[car] == 'C' and today_cars[car] == 'C':
        cars_parked = cars_parked + 1

print(cars_parked)
    

# Three lines of input
    # NUMBER_OF_SPACES
    # number_of_cars
    # today_cars
# for loop that assigns each iteration of a string to a variable