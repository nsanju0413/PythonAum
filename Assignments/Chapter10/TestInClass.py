def main():
    full_name = get_full_name()
    print()
    password = get_password()
    print()
    email = get_email_address()
    print()
    phone_number = get_phone_number()
    print()

    first_name = get_first_name(full_name)
    print(f"Hi {first_name}, thanks for creating an account.")
    print("We'll text your confirmation code to this number: 334.232.6789")
    print()


def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")


def get_email_address():
    while True:
        email = input("Enter email address:      ").strip()
        if "@" in email and "." in email:
            return email
        else:
            print("Invalid email address format. Please enter a valid email address.")


def get_password():
    while True:
        password = input("Enter password:        ").strip()
        digit = False
        cap_letter = False
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or \
                cap_letter == False or \
                len(password) < 8:
            print(f"Password must be 8 characters or more \n"
                  f"with at least one digit and one uppercase "
                  f"letter.")
        else:
            return password


def get_phone_number():
    while True:
        phone_number = input("Enter phone number:       ").strip()
        if phone_number.isdigit() and len(phone_number) == 10:
            return phone_number
        else:
            print("Invalid phone number. Please enter a 10-digit number.")


def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]

    return first_name


if __name__ == "__main__":
    main()
