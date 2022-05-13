#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

## easy level

# password = ""
# for char in range(nr_letters):
#     random_char = random.choice(letters)
#     password += random_char
#
# for char in range(nr_symbols):
#     random_symbol = random.choice(symbols)
#     password += random_symbol
#
# for number in range(nr_numbers):
#     random_number = random.choice(numbers)
#     password += random_number
#
# print(f"your password is {password}")

# Hard level
password_list = []
for char in range(nr_letters):
    random_char = random.choice(letters)
    password_list.append(random_char)
    # password += random_char

for char in range(nr_symbols):
    password_list.append(random.choice(symbols))

for number in range(nr_numbers):
    random_number = random.choice(numbers)
    # password += random_number
    password_list.append(random_number)

# Shuffle the password list
random.shuffle(password_list)

# password variable to add the character from shuffle list
password = ""
for char in password_list:
    password += char

print(f"f Your password is {password}")
