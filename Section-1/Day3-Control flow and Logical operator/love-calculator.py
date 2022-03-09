print("Welcome to Love Calculator!")
name1 = input("What is your Name \n :> ").lower()
name2 = input("What is their Name \n :> ").lower()

combine_string = name1 + name2
t = combine_string.count("t")
r = combine_string.count("r")
u = combine_string.count("u")
e = combine_string.count("e")

true = t + r + u + e
l = combine_string.count("l")
o = combine_string.count("o")
v = combine_string.count("v")
e = combine_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)
print(love_score)