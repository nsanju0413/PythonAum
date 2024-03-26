from datetime import datetime, timedelta

def calculate_travel_time():
    print("Arrival Time Estimator")
    print()
    while True:
        dep_date = input("Estimated date of departure (YYYY-MM-DD): ")
        dep_time = input("Estimated time of departure (HH:MM AM/PM): ")
        dist_miles = int(input("Enter miles: "))
        speed_mph = int(input("Enter miles per hour: "))
        print()

        dep_dt = datetime.strptime(dep_date + ' ' + dep_time, '%Y-%m-%d %I:%M %p')

        travel_hrs = dist_miles // speed_mph
        travel_mins = (dist_miles % speed_mph) * 60 // speed_mph

        arr_dt = dep_dt + timedelta(hours=travel_hrs, minutes=travel_mins)

        print("Estimated travel time")
        print("Hours:", travel_hrs)
        print("Minutes:", travel_mins)
        print("Estimated date of arrival:", arr_dt.strftime('%Y-%m-%d'))
        print("Estimated time of arrival:", arr_dt.strftime('%I:%M %p'))
        print()

        choice = input("Continue? (y/n): ")
        print()
        if choice.lower() != 'y':
            print("Bye!")
            break

if __name__ == "__main__":
    calculate_travel_time()
