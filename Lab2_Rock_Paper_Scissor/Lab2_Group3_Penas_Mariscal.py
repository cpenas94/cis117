# Lab 2
# Group 3
# Authors: Henry Penas, Anthony Mariscal
# Date: 02/17/2023

import random


def guessing_game():
    """
    Author: Henry Penas
    The Guessing Game is a game where a player chooses a random from 1 through 6. The player has 3 tries to choose
    the right number, otherwise the player will lose
    """
    while True:
        print("I'm thinking of a number between 1 and 6.")
        number = random.randint(1, 6)
        tries = 3
        while tries > 0:
            guess = int(input(f"Guess what it is. You have {tries} tries: "))
            if guess == number:
                print("You got it!")
                break
            elif guess < number:
                print(f"Too low, Try again! ({tries - 1} tries left):")
            else:
                print(f"Too high, Try again! ({tries - 1} tries left):")
            tries -= 1
        else:
            print(f"Nope! You lost. The number was {number}")

        play_again = input("Play again? (Y/N): ").upper()
        if play_again == "N":
            return


def rock_paper_scissors():
    """
    Author: Henry Penas
    Rock, Paper, Scissors is a game where a player(user_choice) and the opponent(computer_choice) chooses an option
    (rock, paper or scissors). The program determines who is the winner, loser or if it's tied as defined below.
    """
    while True:
        options = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(options)
        user_choice = input("Choose your option: 1. Rock, 2. Paper, 3. Scissors: ")
        user_choice = options[int(user_choice) - 1]

        print(f"You chose {user_choice} and your opponent chose {computer_choice}.")
        if user_choice == computer_choice:
            print("It is a tie!")
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
                (user_choice == "Paper" and computer_choice == "Rock") or \
                (user_choice == "Scissors" and computer_choice == "Paper"):
            print(f"You win! {user_choice} beats {computer_choice}")
        else:
            print(f"You lose! {computer_choice} beats {user_choice}")

        play_again = input("Play again? (Y/N): ").upper()
        if play_again == "N":
            return


if __name__ == "__main__":
    """
    Author: Henry Penas
    This allows you to choose between the options, Guessing Game, Rock Paper Scissors or to quit the program
    Option 1 goes to the Guessing Game, Option 2 goes to Rock Paper Scissors and Option 3 ends the program
    """
    while True:
        game_choice = int(input("Choose your option: 1. Guessing Game 2. Rock Paper Scissors 3. Quit "))
        if game_choice == 1:
            guessing_game()
        elif game_choice == 2:
            rock_paper_scissors()
        elif game_choice == 3:
            print("Program Ended")
            break
        else:
            print("Not an option")
