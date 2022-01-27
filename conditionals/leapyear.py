###Function to return whether or not an input year is a leap year

def leap_year(year):
    leap = False
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        leap = True
    
    if leap == True:
        print('it is a leap year')
    
    if leap == False:
        print('it is not a leap year')

leap_year(2001)