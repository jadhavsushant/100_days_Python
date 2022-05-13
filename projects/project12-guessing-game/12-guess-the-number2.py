#TODO-1: print the game welcome and baner
GS_EMJ = "🤔🤔🤔"
from operator import truediv
from art import logo
print(logo)
print(f"Welcome to the Number {GS_EMJ[0]} Guessing Game !!")
print("I'm thinking of a number between 1 and 100.")

#TODO-2:print choose difficulty
game_level = str(input("Choose a difficulty. Type 'easy' or 'hard':"))

#TODO-3:validate the receive input

easy = 10
hard = 5

def guess_number():
    """this fucntion return the guess options depend on game_level"""
    guess_attempt = 0
    if game_level == 'easy':
        return easy
    else:
        return hard

turns = guess_number()

import random
def guess_num():
    """Random function to revert the random number"""
    GUESSING_NUMBERS = random.choice(range(1, 100))
    return GUESSING_NUMBERS

random_number = guess_num()


#TODO-4:Create function for easy and Hard
# with random number and create global variable
is_continue = True
while is_continue:
    turns = turns
    print(turns)
    print(f"You have {turns} attempts remeaning to guess the number")
    make_guess = int(input("Make a guess: "))
    if turns <= 0:
       print("You've run out of guesses, you lose.")
       is_continue = False
    
    else:
        if make_guess == random_number:
            print("Well done, your guess is correct")
            is_continue = False
        elif make_guess > random_number:
            print("Too high")
            print("Guess Again")
            turns -= 1
        elif make_guess < random_number:
            print("Too low")
            print("Guess Again")
            turns -= 1
