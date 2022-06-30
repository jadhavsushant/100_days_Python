# working with the file

# with open(file="my_file.txt") as file:
#     content = file.read()
#     print(content)

# write the file

# with open(file="my_file.txt", mode="a") as f:
#     f.write("\n- Writing from python console")

with open(file='C:\\Users\\SushantJadhav\\Desktop\\my_file.txt') as f:
    content = f.read()
    print(content)