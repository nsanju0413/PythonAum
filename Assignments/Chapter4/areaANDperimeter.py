def calculate_area_and_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    print(f'Area: {area} \nPerimeter: {perimeter}')

print("The area and perimeter app\n")
length = float(input('Enter length: '))
width = float(input('Enter width: '))

calculate_area_and_perimeter(length, width)

print('Bye')
