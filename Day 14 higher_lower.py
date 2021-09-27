from art import logo, vs
from game_data import data
import random
import os

# Generate a random account from the game data.
# Format account data into printable format.
# print(f'{name}: {account["follower_count"]}')
def check_answer(answer, a_follower_account, b_follower_account):
    if a_follower_account > b_follower_account:
        return answer == "a"
    else:
        return answer == "b"
        
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_account():
    i = random.randint(0, len(data)-1)
    name = data[i]["name"]
    followers = data[i]["follower_count"]
    description = data[i]["description"]
    country = data[i]["country"]
    #print(f'{name}: {followers}')
    return data[i]

def check_answer(guess, a_follower_account, b_follower_account):
    if a_follower_account > b_follower_account:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    score = 0
    game_should_continue = True
    person_a = get_account()
    person_b = get_account()
    
    while game_should_continue:
        person_a = person_b
        person_b = get_account()
        #person_b = get_account()
        #if person_b != person_a:
        #    break

        print(person_a["name"])
        print(vs)
        print(person_b["name"])

        answer = input(f"Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_account = person_a["follower_count"]
        b_follower_account = person_b["follower_count"]
        is_correct = check_answer(answer, a_follower_account, b_follower_account)

        clear_screen()


        if is_correct:
            score += 1
            print(f"You're right. Current Score {score}")
        else:
            game_should_continue = False
            print(f"Sorry thats wrong. Final Score {score}")

game()




#print(f'{name}: {account["follower_count"]}')

# Ask user for a guess.
#answer = input("Who has more followers, 'A' or 'B'? \n").lower

# Check if user is correct

## Get follower count.

## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds

game()