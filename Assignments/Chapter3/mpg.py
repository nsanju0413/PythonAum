print("Miles per Gallon Application\n")

while True:
    miles_driven = float(input("Enter miles driven:\t"))
    if miles_driven <= 0:
        print("Miles driven must be greater than zero")
    else:
        break

while True:
    gas_used = float(input("Enter gallons of gas used:\t"))
    if gas_used <= 0:
        print("Gas used must be greater than zero")
    else:
        break

while True:
    cost_per_gallon = float(input("Enter cost per gallon:\t"))
    if cost_per_gallon <= 0:
        print("Cost per gallon value must be greater than zero")
    else:
        break

miles_per_gallon = miles_driven / gas_used
tot_gas_used = gas_used * cost_per_gallon
cost_per_mile = tot_gas_used / miles_driven

print("\nMiles per Gallon:\t", round(miles_per_gallon, 1))
print("Total Gas Cost:\t\t", round(tot_gas_used, 1))
print("Cost per Mile:\t\t", round(cost_per_mile, 1))

print("\nBye!")
