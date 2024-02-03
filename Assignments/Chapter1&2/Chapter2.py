print("The Miles Per Gallon Application\n")

miles_driven = float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost=float(input("Enter cost for gallon:\t"))



mpg = miles_driven / gallons_used
mpg = round(mpg, 1)
total_gas=gallons_used*cost
total_gas=round(total_gas,1)
cost_per_mile=total_gas/miles_driven
cost_per_mile=round(cost_per_mile,1)

print("\nMiles Per Gallon:\t\t" + str(mpg))
print("Total Gas Cost:\t\t"+str(total_gas))
print("Cost per Mile:\t\t"+str(cost_per_mile)+"\n")
print("Bye!")



