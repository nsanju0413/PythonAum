class MonthlySales:
    def __init__(self, file_name):
        self.sales = {}
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    month, amount = parts
                    self.sales[month.lower()] = float(amount)
                else:
                    print(f"Ignoring invalid line: {line.strip()}")

    def view_sales(self, month):
        if month.lower() in self.sales:
            print(f"Sales amount for {month.capitalize()} is {self.sales[month.lower()]:,.2f}.")
        else:
            print("Invalid three-letter  month.")

    def edit_sales(self, month, amount):
        if month.lower() in self.sales:
            self.sales[month.lower()] = amount
            print(f"Sales amount for {month.capitalize()} is {self.sales[month.lower()]:,.2f}.")
        else:
            print("Invalid three-letter month.")

    def view_totals(self):
        yearly_total = sum(self.sales.values())
        monthly_average = yearly_total / len(self.sales)
        print(f"Yearly total: {yearly_total:,.2f}")
        print(f"Monthly average is: {monthly_average:,.2f}")


def main():
    file_name = "monthly_sales.txt"  # Assuming the file is always named monthly_sales.txt
    sales_tracker = MonthlySales(file_name)

    print("Monthly Sales Program")
    print("COMMAND MENU")
    print("view  - view sales for specified month")
    print("edit  - edit sales for specified month")
    print("totals - view sales summary for year")
    print("exit  - exit program")

    while True:
        command = input("\ncommand: ").strip().lower()

        if command == "view":
            month = input("three-letter month: ").strip().lower()
            sales_tracker.view_sales(month)
        elif command == "edit":
            month = input("three-letter month: ").strip().lower()
            try:
                amount = float(input("sales amount: "))
                sales_tracker.edit_sales(month, amount)
            except ValueError:
                print("Invalid sales amount. Please enter a numeric value.")
        elif command == "totals":
            sales_tracker.view_totals()
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
