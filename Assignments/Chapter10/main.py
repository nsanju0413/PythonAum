def main():
    full_name = get_fullname()
    password = get_password()
    email = get_email()
    phone = get_phone()
    first_name = get_first_name(full_name)
    formatted_phone = format_phone_number(phone)
    print(f"\nHi {first_name}, thanks for creating an account.\nWe'll text your confirmation code to this number: {formatted_phone}")

def get_fullname():
    while True:
        name = input("Enter full name: ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")


def get_password():
    while True:
        password = input("Enter password: ").strip()
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


def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name


def get_email():
    email = input("Enter your email address: ")
    at_index = email.find("@")
    dot_index = email.find(".", at_index)
    if at_index == -1 or dot_index == -1:
        print("Invalid email address:", email)
    else:
        return email


def get_phone():
    while True:
        phone = input("Enter your phone number: ")
        phone = phone.replace("-", "").replace(" ", "")
        if phone.isdigit() and len(phone) == 10:
            return phone
        else:
            print("Invalid phone number. Please enter a 10-digit numeric phone number.")


def format_phone_number(phone):
    formatted_phone = f"{phone[:3]}.{phone[3:6]}.{phone[6:]}"
    return formatted_phone


if __name__ == "__main__":
    main()
