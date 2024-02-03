import random

def fun():
    print("\t\tNumber Guessing\n")
    print("==============================")
    random_number = random.randint(1, 10)
    attempts = 0

    while True:
        user_input = int(input("Enter the guessing number:\t"))

        if 0 < user_input < 10:
            attempts = attempts + 1

            if random_number == user_input:
                print(f"The number is matched in {attempts} attempts!")
                break
            elif random_number < user_input:
                print("Number is less than the entered value")
            else:
                print("Number is greater than the entered value")

        else:
            print("Enter the number between 1 to 10")
if __name__ == "__main__":
    fun()
