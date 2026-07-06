"""
Introduction to Scripting: Higher/Lower Guessing Game

Player sets a number range, the game picks a secret number within it,
and the player guesses until they find it, with feedback on each guess.

Implemented from original course pseudocode.
"""

import random


def get_range():
    while True:
        lower_limit = int(input("Enter the lower limit: "))
        upper_limit = int(input("Enter the upper limit: "))

        if lower_limit < upper_limit:
            return lower_limit, upper_limit

        print("Invalid range. The lower limit must be less than the upper limit.")


def get_valid_guess(lower_limit, upper_limit):
    guess = int(input(f"Guess a number between {lower_limit} and {upper_limit}: "))

    while guess < lower_limit or guess > upper_limit:
        print(f"Invalid guess. Enter a number between {lower_limit} and {upper_limit}.")
        guess = int(input(f"Guess a number between {lower_limit} and {upper_limit}: "))

    return guess


def main():
    print("Higher/Lower Game")

    lower_limit, upper_limit = get_range()
    secret_number = random.randint(lower_limit, upper_limit)

    guess = get_valid_guess(lower_limit, upper_limit)

    while guess != secret_number:
        if guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

        guess = get_valid_guess(lower_limit, upper_limit)

    print("Correct! You guessed the number.")


if __name__ == "__main__":
    main()
