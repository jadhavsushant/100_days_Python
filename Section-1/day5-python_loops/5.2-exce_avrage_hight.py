# Average hight of students

student_hight = input("input student hights ").split()
# print(student_hight)

total_hights = 0
count = 0
for student in student_hight:
    total_hights = int(total_hights) + int(student)
    count += 1

average_hight = round(total_hights / count)

# print(average_hight)

print(f"Student average hight is {average_hight}")