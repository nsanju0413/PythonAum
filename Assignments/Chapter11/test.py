from datetime import datetime

today = input("Enter today's date: ")

this_day = datetime.strptime(today, "%m/%d/%Y")

print(this_day)