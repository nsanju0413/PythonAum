def mpg(miles, gallons, cost):
    miles_per_gallon = miles / gallons
    total_gas_cost = gallons * cost
    cost_per_mile = total_gas_cost / miles
    print('Miles per gallon:', round(miles_per_gallon, 1))
    print('Total gas cost:', round(total_gas_cost, 1))
    print('Cost per mile:', round(cost_per_mile, 1))

print("The Miles Gallon Application\n")
miles = float(input('Enter miles driven: '))
gallons = float(input('Enter gallons of gas used: '))
cost = float(input('Enter cost per gallon: '))

mpg(miles, gallons, cost)

print('Bye')
