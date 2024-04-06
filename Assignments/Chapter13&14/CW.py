def natural_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def natural_square_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total

def main():
    while True:
        user_input = input("Enter nbr for naturalSum: ").strip().lower()
        if user_input == 'n':
            print("Bye!")
            break

        num = user_input
        if not num.isdigit():
            print("Invalid input. Please enter a number")
            continue

        num = int(num)
        print(f"NaturalSum {num} is {natural_sum(num)}")
        print(f"NaturalSqrSum {num} is {natural_square_sum(num)}")

        continue_input = input("\nContinue (Y/N): ").strip().lower()
        if continue_input != 'y':
            print("Bye!")
            break

if __name__ == "__main__":
    main()
