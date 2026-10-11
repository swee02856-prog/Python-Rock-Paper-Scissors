import RockSystem
import PaperSystem
import ScissorsSystem
import LifeSystem
import PlayAgainOrContinue
import UserChoice
import ComputerChoice
import Voicelines
from RockSystem import Rock
from PaperSystem import Paper
from ScissorsSystem import Scissors
from LifeSystem import Life
import random
from PlayAgainOrContinue import ask_play_again
from UserChoice import get_user_choice
from LifeSystem import ComputerLife

# Establish our modules and functions

def Characters():
    print("Who do you wanna run the 1's with?")
    print("1. Jimmy the Joker\n2. Timmy le destroyer\n3. Billy Badass")
    choice = input("Enter your choice (1-3): ")
    return choice

def Computer_level_choice():
    if character_choice == "1":
        return GG_fucking_easy()
    elif character_choice == "2":
        return medium()
    elif character_choice == "3":
        return hard()
    else:
        print("Error: Invalid Character routing to Regular (Medium)")
        return medium()

def GG_fucking_easy():
    if UserChoice == Rock():
            return random.choice([Scissors(), Rock()])
    elif UserChoice == Paper():
            return random.choice([Rock(), Paper()])
    elif UserChoice == Scissors():
            return random.choice([Paper(), Scissors()])
    return random.choice([Rock(), Paper(), Scissors()])
def medium():
    choices = [Rock(), Paper(), Scissors()]
    return random.choice(choices)
def hard():
    choices = [Rock(), Paper(), Scissors()]
    if UserChoice == Rock():
        return random.choice([Paper(), Rock()])
    elif UserChoice == Paper():
        return random.choice([Rock(), Paper()])
    elif UserChoice == Scissors():
        return random.choice([Rock(), Scissors()])
    return random.choice(choices)


print("Welcome to Rock, Paper, Scissors!")

character_choice = Characters()
print(character_choice)

def Voiceline():
    return Voicelines.CharacterVoiceline(character_choice)

def Greeting():
    return Voicelines.CharacterGreeting(character_choice)

print(Greeting())

GameRunning = True
Lives = Life()
ComputerLives = ComputerLife()
while GameRunning == True and (Lives > 0 or ComputerLives > 0):
    input("Press Enter to start the game...")

    UserChoice = get_user_choice()
    print(UserChoice)

    input("Press to get Computer's Choice...")
    ComputerChoice = Computer_level_choice()
    print(ComputerChoice)

    print(Voiceline())

    input("Press Enter to see the result...")
    
    def GameRules():
        global Lives, ComputerLives
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
    print(f"You have {Lives} lives!")
    print(f"Computer has {ComputerLives} lives!")

    if Lives == 0:
        print("You have run out of lives!")
        GameRunning = False
    if ComputerLives == 0:
        print("Computer has run out of lives!")
        GameRunning = False

    if GameRunning:
        GameRunning = ask_play_again()