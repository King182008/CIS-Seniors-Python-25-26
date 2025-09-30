'''
File: Number Guessing Game
Name: Xaiden Morey
Date: 9/30/2025
Class: CIS Seniors
'''

import random

# Function to start the game
def start_game():
    print("Welcome to the number guessing game.")

    # Computer chooses a random number
    number_to_guess = random.randint(1, 100)

    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1 - 100): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congrats! You guessed the number {number_to_guess} in {attempts} attempts.")
            break

if __name__ == "__main__":
    start_game()