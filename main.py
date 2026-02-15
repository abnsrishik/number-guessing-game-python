from art import logo
import random

print(logo)
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# check the difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

chance = 0
# set random number to guess
number = random.randint(1,100)

def easy():
    # chances 10 for easy mode
    chance = 10
    game_over = False
    while not game_over: # run until chances = 0 or number = guess
        print(f"You have {chance} attempts remaining to guss the number.")
        guess = int(input("Make a guess: "))
        if number != guess:
            chance -= 1
            if guess < number:
                print("Too Low")
            elif guess > number:
                print("Too High")
        if number == guess:
            print(f"You got it! The answer was {number}")
            game_over = True
        if chance == 0:
            print(f"You've run out of guesses. Refresh the page to run again.")
            game_over = True
def hard():
    chance = 5 # 5 chances for hard mode
    game_over = False
    while not game_over:
        print(f"You have {chance} attempts remaining to guss the number.")
        guess = int(input("Make a guess: "))
        if number != guess:
            chance -= 1
            if guess < number:
                print("Too Low")
                print("Guess Again")
            elif guess > number:
                print("Too High")
                print("Guess Again")
        if number == guess:
            print(f"You got it! The answer was {number}")
            game_over = True
        if chance == 0:
            print(f"You've run out of guesses. Refresh the page to run again.")
            game_over = True

if difficulty == 'easy':
    easy()
elif difficulty == 'hard':
    hard()
else:
    print("Invalid Input")
