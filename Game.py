import RockSystem
import PaperSystem
import ScissorsSystem
from RockSystem import Rock
from PaperSystem import Paper
from ScissorsSystem import Scissors
import random

def get_computer_choice():
    choices = [Rock, Paper, Scissors]
    return random.choice(choices)()

def get_user_choice():
    user_input = input("Choose Rock, Paper, or Scissors: ").lower()
    if user_input == "rock":
        return Rock()
    elif user_input == "paper":
        return Paper()
    elif user_input == "scissors":
        return Scissors()
    else:
        print("Invalid choice. Please try again.")
        return get_user_choice()

print("Welcome to Rock, Paper, Scissors!")
    
GameRunning = True
while GameRunning == True:
    input("Press Enter to start the game...")

    UserChoice = get_user_choice()
    print(UserChoice)

    input("Press to get Computer's Choice...")
    ComputerChoice = get_computer_choice()
    print(ComputerChoice)

    input("Press Enter to see the result...")

    def GameRules():
        if UserChoice == ComputerChoice:
            return("Tie!")

        elif UserChoice == Rock() and ComputerChoice == Scissors():
            return("You win!")
        elif UserChoice == Paper() and ComputerChoice == Rock():
            return("You win!")
        elif UserChoice == Scissors() and ComputerChoice == Paper():
            return("You win!")
        else:
            return("Computer wins!")
    print(GameRules())

    def ask_play_again():
        play_again = input("Do you want to continue? Y/N: ").lower()
        if play_again == "y":
            return True
        elif play_again == "n":
            print("Thanks for playing!")
            return False
        else:
            print("Invalid input. Please try again.")
            return ask_play_again()

    GameRunning = ask_play_again()