total_megabytes = int(input('How much phone data is Hamilton given a month as part of his monthly phone plan?: '))
total_months = int(input('How many months has Hamilton had this phone plan?: '))

excess = 0

for i in range(total_months):
    print(i)
    print(f'Excess: {excess}')
    used = int(input('How much data was used this month?: '))
    print(f'Used:{used}')
    excess = excess + total_megabytes - used
    print(f'Monthly Megabytes:{total_megabytes}')
    print(f'Months with plan:{total_months}')

#   This prints the total amount of megabytes available for next month
print(excess + total_megabytes)