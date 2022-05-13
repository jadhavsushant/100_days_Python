# collect random number from 1-100
from random import randint
from art import logo

## GLOBAL VARIABLES
EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


## fucntion to check guess from actual answer
def check_answer(guess, answer, turns):
    if guess > answer:
        print("To high.")
        return turns -1
    elif guess < answer:
        print("To Low")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}.")

# Make functionality to set dificulty
def set_dificulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN

def game():
    print(logo)
    print("Welcome to the Number 🤔 Guessing Game !!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_dificulty()

    #Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
       print(f"You have {turns} attempts remaining to guess the number.")

       #Let the user guess a number.
       guess = int(input("Make a guess: "))

       turns = check_answer(guess, answer, turns)

       if turns == 0:
           print("You've run out of guesses, you lose.")
           return
       elif turns != answer:
           print("Guess again.")


game()