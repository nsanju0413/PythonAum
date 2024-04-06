import classXYZ as y

def main():
    print("BMI Calculation using Class")
    while True:
        height = float(input("\nEnter height in inches: "))
        weight = float(input("Enter weight in pounds: "))

        bmi_calculator = y.BMI(height, weight)
        bmi_description = bmi_calculator.bmi_description()

        print(f"Person is {bmi_description}")

        user_input = input("\nContinue (Y/N): ").lower()
        if user_input == 'n':
            print("Bye!")
            break

if __name__ == "__main__":
    main()