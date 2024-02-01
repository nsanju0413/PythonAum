def my_function():
    print("The Miles Per Gallon Application")
    miles=int(input("Enter miles driven:\t"))
    gallons=int(input("Enter gallons of gas used:\t"))
    cost=float(input("Enter cost per gallon:\t"))

    miles_per_gallon=miles/gallons
    miles_per_gallon=round(miles_per_gallon,1)
    print("\n\nMiles per gallon:\t"+str(miles_per_gallon))
    total_gas = gallons * cost
    total_gas=round(total_gas,1)
    print("Total Gas cost:\t"+str(total_gas))
    cost_per_mile = total_gas / miles
    cost_per_mile = round(cost_per_mile, 1)
    print("Cost per mile:\t"+str(cost_per_mile))

    print("\nBye!!")

my_function()