# Write a program in Python to check if a year is leap or not

year = int(input("Enter the year : "))

#Condition of century year and a leap year
if (year%400 == 0) and (year%100 == 0):
    print("{0} is a leap year".format(year))
#Condition for  checking that a year is leap year but not a century year
elif (year%4 == 0) and (year%100!=0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))         