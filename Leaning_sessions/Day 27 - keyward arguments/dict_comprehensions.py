keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]

my_d = dict(zip(keys, values))
print(my_d)
for k in my_d:
    print(k, my_d[k])

# comprehension
myDict = {k: v for (k, v) in zip(keys, values)}

print(myDict)

# creation using list comprehension
myDict = {x: x ** 2 for x in [1, 2, 3, 4, 5]}
print(myDict)

# and like
sDict = {x.upper(): x * 3 for x in "coding"}
print(sDict)

# We can use Dictionary comprehensions with if and else statements and with other expressions too.
# This example below maps the numbers to their cubes that are not divisible by 4:

newDict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newDict)


# testing uppers
prompt_response = str(input("Enter your name?"))
dict = {'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf',"H":"Hotel", 'I':'India', 'J':'Juliet', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}
sDict = {x.upper(): dict[x.upper()] for x in prompt_response}
print(sDict)


