""""
Write a program that works out whether if a given year is leap year.
"""

year = int(input("Which year you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("this is leaf year")
        else:
            print("This is not leaf year")
    else:
        print("This is not leaf year")
else:
    print("This is not leaf year")