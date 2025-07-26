from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date)
display_current_datetime()

def calculate_future_date():
    days = int(input("Add the number of days to add to current date: "))
    future_date = datetime.now() + timedelta(days =days)
    return future_date

display_current_datetime()
print("Future_date:", calculate_future_date())

