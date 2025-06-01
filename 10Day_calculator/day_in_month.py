def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# TODO: Add more code here 👇
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2:
        is_leap_year = is_leap(year)
        if is_leap_year:
            return month_days[1] + 1
        else:
            return month_days[1]
    else:
        return month_days[month - 1]


year = int(input())  # Enter a year
month = int(input())  # Enter a month
day = -1
if month > 12:
    print("Invalid input data. We have only 12 months")
elif month < 1:
    print("Invalid input data. Month number can't be less then 1.")
else:
    days = days_in_month(year, month)

print(days)

