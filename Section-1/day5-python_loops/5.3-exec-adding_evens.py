# sum of even numbers using range function

even_number_total = 0

# for number in range(2, 101, 2):
#     even_number_total += number
# print(even_number_total)

for number in range(1, 101):
    if number % 2 == 0:
        even_number_total += number
print(even_number_total)