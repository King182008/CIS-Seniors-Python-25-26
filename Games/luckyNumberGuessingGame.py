'''
File: Lucky Number Guessing Game
Name: Xaiden Morey
Class: CIS Seniors
Date: 10/2/2025
'''

import random

# Game statistics
total_rounds = 0
total_wins = 0
total_guesses = 0

print("=" * 50)
print("  WELCOME TO THE LUCKY NUMBER GUESSING GAME!")
print("=" * 50)
print()

# Main game loop - play multiple rounds
while True:

    # Generate random lucky number
    number_to_guess = random.randint(1, 50)

    # Set maximum attempts
    max_attempts = 7

    # Initialize attempt counter
    attempts = 0
    
    print(f"\nRound {total_rounds + 1}")
    print("I'm thinking of a lucky number between 1 and 50...")
    print(f"You have {max_attempts} attempts to guess it!")
    print()
    
    # Guessing loop - count-controlled while loop
    while attempts < max_attempts:
        userGuess = int(input("Enter your guess: "))
        attempts += 1
        total_guesses += 1
        if userGuess == number_to_guess:
            print("Congratulations, You won in", attempts, "tries!")
            win = "True"
            total_wins += 1
            break
        elif userGuess > number_to_guess:
            print("Too High, try again\n")
        elif attempts == max_attempts:
            print("You failed to guees within the alloted attempts, you lose.")
            win = "False"
            break
        else:
            print("Too Low, try again!\n")

    # Display round statistics
    print("Attempts:", attempts)
    print("Won:", win)
    total_rounds += 1
    # Ask if player wants to play again
    playAgain = input("Would you like to play again? (yes/no) ")
    if playAgain == "no" or "No":
        break
    else:
        attempts = 0
# Display final statistics
print("\n\n\n")
print("Total Rounds:", total_rounds)
print("Total Wins:", total_wins)
print("Average Guesses per Round:", (total_guesses / total_rounds))

print("\nThanks for playing! Goodbye!")