#Chapter 1 Assignment
import locale
result = locale.setlocale(locale.LC_ALL, '')
if result == 'C' or result.startswith('C/'):
    locale.setlocale(locale.LC_ALL, 'en_US')


print("\n\nWelcome to the Future Value Calculator\n")
choice="y"
while choice.lower()=="y":
    monthly_investment=float(input("Enter monthly investment:\t"))
    yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
    years = int(input("Enter number of years:\t\t"))
    monthly_insterest_rate = yearly_interest_rate / 12 / 100
    months = years * 12
    future_value = 0

    for i in range(months):
        future_value = future_value + monthly_investment
        monthly_interest_amount = future_value * monthly_insterest_rate
        future_value = future_value + monthly_interest_amount

    print("Future value:\t\t\t" + locale.currency(future_value, grouping=True))

    choice = input("\nContinue? (y/n): ")

print("\nBye!")