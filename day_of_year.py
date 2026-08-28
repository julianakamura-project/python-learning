def is_year_leap(year):
    if year%4 != 0:
        return False
    elif year%100 != 0:
        return True
    elif year%400 != 0:
        return False
    return True

def days_in_month(year, month):
    if month == 2:
        if is_year_leap(year):
            return 29
        return 28
    if month <= 7:
        if month%2 == 0:
            return 30
        return 31
    elif month%2 == 0:
        return 31
    return 30

def valid_date(month, day):
    if day == 0 or day > 31:
        return False
    if (is_year_leap == False and month == 2 and day > 28):
        return False
    if month <= 7:
        if month%2 == 0 and day == 31:
            return False
        return True
    elif month%2 != 0 and day == 31:
        return False
    return True

def day_of_year(year, month, day):
    day = 0
    for i in range(1, month+1):
        day += days_in_month(year, i)
    return day

year = int(input("Please enter a year: "))
month = int(input("Please enter a month (1-12): "))
day = int(input("Please enter a day (1-31): "))

if valid_date(month, day) == False:
    print("Invalid date.")

else:
    date = day_of_year(year, month, day)
    print(f"This day is corresponds to day {date} of the year.")