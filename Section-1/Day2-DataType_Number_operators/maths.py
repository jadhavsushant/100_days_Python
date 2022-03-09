# print(3 + 5)
# print(3 - 7)
# print(3 * 5)
# print(9 / 3)
# print(2 ** 4)

# maths operaters calculation happens on this.
# PEMDASLR
# () - pranthasis (higest priority)
# ** - exponential
# * - multiplication
# / - subsctraction
# +  - addition
# -  - division (lowest priority)

# BMI caclulator

height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
bmi = int( weight / (height ** 2))
# bmi = int(weight) / float(height) **2
# bmi_as_int = int(bmi)
print(bmi)