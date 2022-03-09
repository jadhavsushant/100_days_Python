# Check the odd or even number
# number = int(input("which number do you want to check? "))
#
# if number % 2 == 0:
#     print("this is an even number")
# else:
#     print("this is an odd number")

# height and ticket checker
# print("welcome to HM Roller Coaster")
# height = int(input("whats your height in cm: "))
#
# if height >= 120:
#     print(" Woooo,  you can take a ride")
#     age = int(input(" whats your age? "))
#     if age > 18:
#         print("Please pay $18.")
#     elif age < 12:
#         print("Please pay $5 ")
#     else:
#         print("Please pay $7.")
# else:
#     print(" Sorry, you need to grow taller to take ride")

# BMI calculator 2.0
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# BMI = int(weight / ( height **2) )
bmi_as = round(weight / (height ** 2))
# print(round(bmi_as))
# print(bmi_as)
if  bmi_as < 18.5:
    print(f"Your bmi is {bmi_as}, you are underweight")
elif bmi_as < 25:
    print(f"Your bmi is {bmi_as}, you are normal weight")
elif bmi_as < 30:
    print(f"Your bmi is {bmi_as}, you are overwight")
elif bmi_as < 35:
    print(f"Your bmi is {bmi_as}, you are obse")
else:
    print(f"Your bmi is {bmi_as}, efinically obese")