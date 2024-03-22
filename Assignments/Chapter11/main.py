from datetime import datetime, timedelta


def calculate_travel_time():
    while True:
        departure_date = input("Estimated date of departure (YYYY-MM-DD): ")
        departure_time = input("Estimated time of departure (HH:MM AM/PM): ")
        miles = int(input("Enter miles: "))
        mph = int(input("Enter miles per hour: "))

        departure_time = datetime.strptime(departure_time, '%I:%M %p')
        departure_datetime = datetime.strptime(departure_date + ' ' + departure_time.strftime('%I:%M %p'),
                                               '%Y-%m-%d %I:%M %p')

        travel_hours = miles // mph
        travel_minutes = (miles % mph) * 60 // mph

        arrival_datetime = departure_datetime + timedelta(hours=travel_hours, minutes=travel_minutes)

        print("Estimated travel time")
        print("Hours:", travel_hours)
        print("Minutes:", travel_minutes)
        print("Estimated time of arrival:", arrival_datetime.strftime('%I:%M %p'))

        choice = input("Continue? (y/n): ")
        if choice.lower() != 'y':
            print("Bye!")
            break


if __name__ == "__main__":
    calculate_travel_time()
