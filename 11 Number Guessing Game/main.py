import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")

computer_guess=random.randint(1, 100)

difficulty = input("Choose the difficulty. Type 'easy' or 'hard': ")
total_attempts = -1
if difficulty == "easy":
    total_attempts = 10
elif difficulty == "hard":
    total_attempts = 5
else:
    print("Good bey!")

user_guess = -1
while total_attempts > 0:
    print(f"You have {total_attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if computer_guess > user_guess:
        print("Too low.")
    elif computer_guess < user_guess:
        print("Too high.")
    else:
        print(f"You got it! The answer was {computer_guess}.")
        break
    total_attempts -= 1

    if total_attempts > 0:
        print("Guess again.")

if computer_guess != user_guess and total_attempts == 0:
    print("You've run out of guesses. Refresh the page to run again.")