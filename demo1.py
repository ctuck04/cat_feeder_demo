import datetime
import time

def schedule_feeding():
    feeding_time = input("Please enter the feeding time in HH:MM format (24-hour clock): ")
    while True:
        try:
            feeding_hour, feeding_minute = map(int, feeding_time.split(":"))
            break
        except ValueError:
            feeding_time = input("Invalid input. Please enter the feeding time in HH:MM format (24-hour clock): ")
    feeding_date = datetime.date.today()
    feeding_datetime = datetime.datetime.combine(feeding_date, datetime.time(hour=feeding_hour, minute=feeding_minute))
    print(f"Scheduling feeding for {feeding_datetime}")
    now = datetime.datetime.now()
    while now < feeding_datetime:
        time.sleep(1)
        now = datetime.datetime.now()
    print("Feeding time!")
    # Add code here to trigger the feeding mechanism for the cat

schedule_feeding()
