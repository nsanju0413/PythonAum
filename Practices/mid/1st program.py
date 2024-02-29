import math
def calculate_circle_properties(radius):
    circle_area = math.pi * radius ** 2
    circle_perimeter = 2 * math.pi * radius
    return circle_area, circle_perimeter
def main():
    print("The Circle Program\n")
    while True:
        radius_input = input("Enter Radius: ")
        if not radius_input.isdigit() and radius_input[0] != '-':
            print("Wrong input entered")
            continue

        radius = float(radius_input)
        if radius < 0:
            print("Wrong input entered")
            continue

        area, perimeter = calculate_circle_properties(radius)
        print(f"Area of circle:  {area:.2f}")
        print(f"Perimeter of circle: {perimeter:.2f}")

        cont = input("Continue (y/n)? ").lower()
        if cont != 'y':
            print("Bye")
            break

if __name__ == "__main__":
    main()
