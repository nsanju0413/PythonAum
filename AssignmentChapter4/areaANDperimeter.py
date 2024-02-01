def myfun():
    print("The area and Perimeter Application\n")

    length=float(input("Please enter the length:\t"))
    width=float(input("Please enter the width:\t"))

    area = length * width
    perimeter = 2 * (length + width)

    print("\nArea = " + str(area))
    print("Perimeter = " + str(perimeter))

    print(("\nBye!"))

def main():
    myfun()

if __name__=="__main__":
    main()