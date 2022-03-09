print(" ******** welcome to learn pizza hut *********** ")
# pizza price
s_pizza = 15
m_pizza = 20
l_pizza = 25

# total bill
total_bill = 0

# adding Rupees symbol
rupees = u"\u20B9"

size = input("What size of pizza do you want? S, M or L : ")
if size == "S":
    total_bill += s_pizza
    print(f"The small pizza price is {s_pizza} {rupees}")

if size == "M":
    total_bill += m_pizza
    print(f"The medium pizza price is  {m_pizza} {rupees}")

if size == "L":
    total_bill += l_pizza
    print(f"The large pizza price is {l_pizza} {rupees}")

add_pepperoni = input("Do you want Pepperoni? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")
if size == "S" and add_pepperoni == "Y" and extra_cheese == "Y":
    total_bill = s_pizza + 3 + 1
elif size == "M" and add_pepperoni == "Y" and extra_cheese == "Y":
    total_bill = m_pizza + 3
else:
    total_bill += 3

# if extra_cheese == "Y":
#     total_bill += 1

print(f"Your total bill = {total_bill} {rupees}")

