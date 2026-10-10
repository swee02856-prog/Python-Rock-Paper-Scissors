import RockSystem
import PaperSystem
import ScissorsSystem
import LifeSystem
import PlayAgainOrContinue
import UserChoice
import ComputerChoice
from RockSystem import Rock
from PaperSystem import Paper
from ScissorsSystem import Scissors
from LifeSystem import Life, ComputerLife
import random
from PlayAgainOrContinue import ask_play_again
from UserChoice import get_user_choice
from ComputerChoice import get_computer_choice

print("Welcome to Rock, Paper, Scissors!")

GameRunning = True
Lives = Life()
ComputerLives = ComputerLife()
while GameRunning == True and (Lives > 0 or ComputerLives > 0):
    input("Press Enter to start the game...")

    UserChoice = get_user_choice()
    print(UserChoice)

    input("Press to get Computer's Choice...")
    ComputerChoice = get_computer_choice()
    print(ComputerChoice)

    input("Press Enter to see the result...")

    def GameRules():
        global ComputerLives, Lives
        if UserChoice == ComputerChoice:
            return("Tie!")
        elif UserChoice == Rock() and ComputerChoice == Scissors():
            ComputerLives -= 1
            return("You win!")
        elif UserChoice == Paper() and ComputerChoice == Rock():
            ComputerLives -= 1
            return("You win!")
        elif UserChoice == Scissors() and ComputerChoice == Paper():
            ComputerLives -= 1
            return("You win!")
        else:
            Lives -= 1
            return("Computer wins!")
    print(GameRules())

    print(f"You have {Lives} Lives remaining.")
    print(f"Computer has {ComputerLives} Lives remaining.")

    if Lives == 0:
        print("Game over! You have run out of lives.")
        GameRunning = False
    if ComputerLives == 0:
        print("Game over! Computer has run out of lives.")
        GameRunning = False

    if GameRunning:
        GameRunning = ask_play_again()