""""
If
"""
# height and ticket checker
print("welcome to HM Roller Coaster")
height = int(input("whats your height in cm: "))
bill = 0

if height >= 120:
    print(" Wow,  you can take a ride")
    age = int(input(" whats your age? "))
    if age > 18:
        bill = 18
        print("Adult ticket are $18.")
    elif age < 12:
        bill = 5
        print("Child ticket are $5 ")
    else:
        bill = 7
        print("Youth ticket are $7.")

    want_photo = input("do you want to photo type Y or N ?")
    if want_photo == "Y":
        bill += 3

    print(f"Your total bill is {bill}")
else:
    print("Sorry, you need to grow taller to take ride")
