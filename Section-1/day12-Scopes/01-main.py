# scopes 
# GLobal vs Local

# local scope exist within fucntion

def drink_potion():
    potion_strength = 2
    return potion_strength

print(f"Local Scope variable:", drink_potion())

### global variable ##

from dataclasses import replace
from os import access
from traceback import print_tb
from xxlimited import new
# from anywhere from the code file.
# this mean global variable can access from within function and outside function.

global_variable = "Hello_global"

def my_function():
    my_fucntion_var = 10
    print (f"global varible from function:- {global_variable}")

#calling the fucntion
my_function()

print("global variable from outside :", global_variable)


## call from nested fucntion #####

players = "players in game : 11"

def ipl_team():
    def in_playes():
        print(players)

ipl_team()

## the above function will print none
# the neasted fucntion need to call the child function outside of the function.

players = "players in game : 11"

def ipl_team():
    def in_playes():
        print(players)

    in_playes()


ipl_team()


##################################### block scope ###################

# python don't have block scope

players = ["MSD", "Rohit", "Rahul"]
team = "csk"
if team == "csk":
    capton = players[0]

print(capton)

# there is no block of scope like other programming language - we can call from outside statement.

# IMP: If we are creating the variable within the fucntion then it will be avaiable within that funciton.

team = "mi"

def team_caption():
    players = ["MSD", "Rohit", "Rahul"]
    if team == "mi":
        new_caption = players[1]
    
    print(new_caption)

# print(new_caption) ## this will not work 
team_caption()


########################## 😵‍💫 How to modify the global scope  😵‍💫 #################

# 🤩🤩🤩🤩🤩 example 🤩🤩🤩🤩
#global_scope
csk_capton = "MSD"

def new_capton():
    new_capton_csk = "Jadeja"
    print(f"Capton var from inside fucntion: {new_capton_csk}")

new_capton()
print(f"Caption var from outside fucntion: {csk_capton}")


## modify the scope 😵😵😵😵😵😵😵😵😵😵😵😵😵😵

csk_capton = "MSD"

def new_capton():
    print(f"Capton var from inside fucntion: {csk_capton}")
    return csk_capton + " Dhoni"

print(f"Caption var from outside fucntion: {csk_capton}")
csk_capton = new_capton()

print(f"capton variable after modify: {csk_capton}")

## 🤡 While return fucntion we can modify the global variable and reassign it to variable.


########################## 😵‍💫 define the constant  😵‍💫 #################
# The constants mean you will never going to change the variables for assigned to global.
# then you can use the upper case variable for it such as

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@susjadhav"

# when you will use this type of variable it will be easily understand by upper case
# these are global scope variables.

