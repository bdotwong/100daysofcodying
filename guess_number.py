import random
import os
#from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"{guess} was the answer")    

def set_difficulty():
    level = input("Choose diffculty. Type 'easy' or 'hard': \n")
    if level == "easy":
      return EASY_LEVEL
    else: 
      return HARD_LEVEL

def game():
    #print logo
    print("Welcome to the number guessing game")
    print("Pick a number between 1 and 100")
    answer = random.randint(1, 100)
    #print(f"{answer} is answer")

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} left.")
    
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You're out of guesses. You lose. Good day sir")
            return
        elif guess != answer:
            print("Guess again.")
game()