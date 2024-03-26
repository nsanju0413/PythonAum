from datetime import datetime


def get_correct_birth_date(birth_date_str):
    try:
        current_year = datetime.now().year
        birth_date = datetime.strptime(birth_date_str, "%m/%d/%y")
        if birth_date.year > current_year:
            birth_date = birth_date.replace(year=current_year)
        return birth_date
    except ValueError:
        print("Invalid date format. Please enter the birth date in MM/DD/YY format.")
        return None


def calculate_age(birth_date):
    current_date = datetime.now()
    age_years = current_date.year - birth_date.year
    if current_date.month < birth_date.month or (
            current_date.month == birth_date.month and current_date.day < birth_date.day):
        age_years -= 1
    return age_years


def calculate_days_until_birthday(birth_date):
    current_date = datetime.now()
    next_birthday = birth_date.replace(year=current_date.year)
    if next_birthday < current_date:
        next_birthday = next_birthday.replace(year=current_date.year + 1)
    days_until_birthday = (next_birthday - current_date).days

    return days_until_birthday


def main():
    print("Birthday Calculator")
    print()
    while True:
        person_name = input("Enter name: ")
        birth_date_str = input("Enter birthday (MM/DD/YY): ")

        birth_date = get_correct_birth_date(birth_date_str)
        if birth_date is None:
            continue

        age = calculate_age(birth_date)
        days_until_birthday = calculate_days_until_birthday(birth_date)

        print(f"Birthday: {birth_date.strftime('%A, %B %d, %Y')}")
        print("Today:", datetime.now().strftime('%A, %B %d, %Y'))

        if age > 2:
            print(f"{person_name} is {age} years old.")
        else:
            age_days = (datetime.now() - birth_date).days
            print(f"{person_name} is {age_days} days old.")

        if days_until_birthday == 0:
            print(f"{person_name}'s birthday is today!")
        elif days_until_birthday == 1:
            print(f"{person_name}'s birthday is tomorrow!")
        elif days_until_birthday == -1:
            print(f"{person_name}'s birthday was yesterday!")
        else:
            print(f"{person_name}'s birthday is in {days_until_birthday} days.")

        continue_choice = input("Continue? (y/n): ").lower()
        print()
        if continue_choice != 'y':
            print("Bye!")
            break


if __name__ == "__main__":
    main()
