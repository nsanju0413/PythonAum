import csv

def create_email(first_name, last_name):
    return f"{first_name.lower()}_{last_name.lower()}@example.com"

def generate_email(to_email, first_name):
    from_email = "noreply@deals.com"
    subject = "Deals!"
    message = f"Hi {first_name},\n\nWe've got some great deals for you. Check our website!\n"
    email = f"To: {to_email}\nFrom: {from_email}\nSubject: {subject}\n\n{message}"
    return email

def main():
    file_path =r'input.csv'
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            first_name = row['FIRST NM']
            last_name = row['LAST NM']
            to_email = row['EMAIL']
            email_message = generate_email(to_email, first_name)
            print(email_message)

if __name__ == "__main__":
    main()

