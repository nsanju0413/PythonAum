import locale

result = locale.setlocale(locale.LC_ALL, '')
if result == 'C' or result.startswith('C/'):
    locale.setlocale(locale.LC_ALL, 'en_US')

choice = "y"
while choice.lower() == "y":
    monthly_investment = float(input("Enter monthly investment: "))
    yearly_interest_rate = int(input("Enter yearly interest rate: "))
    years = int(input("Enter number of years: "))

    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12
    future_value = 0

    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

    formatted_monthly_investment = locale.currency(monthly_investment, grouping=True)
    formatted_future_value = locale.currency(future_value, grouping=True)

    print(f"\n{('Monthly investment:'): <20}{formatted_monthly_investment: >10}")
    print(f"{('Interest rate:'): <20}{yearly_interest_rate: >10}")
    print(f"{('Years:'): <20}{years: >10}")
    print(f"{('Future value:'): <20}{formatted_future_value: >10}")

    choice = input("\nContinue? (y/n): ")

print("\nBye!")
