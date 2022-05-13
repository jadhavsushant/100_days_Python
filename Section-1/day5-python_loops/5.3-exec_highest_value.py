highest_value = input("input student hights ").split()
# print(student_hight)

highest_score = 0
for score in highest_value:
    if score > highest_score:
        highest_score = score

print(f"The Highest score is {highest_score} ")
