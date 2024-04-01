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
                    print(f"Ignoring  invalid line: {line.strip()}")

    def view_sales(self, month):
        if month.lower() in self.sales:
            print(f"Sales amount for {month.capitalize()} is {self.sales[month.lower()]:,.2f}.")
        else:
            print("Invalid three-letter month.")

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
        print(f"Monthly average: {monthly_average:,.2f}")


def main():
    file_name = "monthly_sales.txt"  # File name to read sales data
    sales_tracker = MonthlySales(file_name)

    print("Monthly Sales program\n")
    print("COMMAND MENU")
    print("view  - View sales for specified month")
    print("edit  - Edit sales for specified month")
    print("totals - View sales summary for year")
    print("exit  - Exit program")

    while True:
        command = input("\nCommand: ").strip().lower()

        if command == "view":
            month = input("Three-letter Month: ").strip().lower()
            sales_tracker.view_sales(month)
        elif command == "edit":
            month = input("Three-letter Month: ").strip().lower()
            amount = float(input("Sales Amount: "))
            sales_tracker.edit_sales(month, amount)
        elif command == "totals":
            sales_tracker.view_totals()
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
