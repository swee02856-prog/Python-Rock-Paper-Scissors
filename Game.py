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

print(get_computer_choice())