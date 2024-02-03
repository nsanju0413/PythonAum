print("The Area and Perimeter App\n")

while True:
    length = float(input("Please enter the length:\t"))
    if length <= 0:
        print("Length must be positive")
    else:
        break

while True:
    width = float(input("Please enter the width:\t"))
    if width <= 0:
        print("Width must be positive")
    else:
        break

area = length * width
perimeter = 2 * (length + width)

print("\nArea:\t\t", area)
print("Perimeter:\t", perimeter)
print("\nBye!")
