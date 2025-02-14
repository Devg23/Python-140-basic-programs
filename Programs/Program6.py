# Write a python program calender

import calendar

month  = int(input("Enter the Month: "))
year = int(input("Enter the year"))

cal = calendar.month(year,month)

print(cal)
