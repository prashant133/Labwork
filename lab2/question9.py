'''
Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else print ‘COMMON YEAR’.
Hint: • a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
• a year is always a leap year if its number is exactly divisible by 400
'''
year = int(input("enter the year: "))
if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 == 0 :
            print(year,'leap year')
        else:
            print(year,'comman year')
    else:
        print(year,'leap year')
else:
    print(year,'comman year')

#using standard libary

# importing calendar library
import calendar

# Reading year from user
year = int(input('Enter year: '))

# Calling isleap() method on calendar library
isLeap = calendar.isleap(year)

# Taking decision
if isLeap:
    print('LEAP YEAR')
else:
    print('NOT LEAP YEAR')
