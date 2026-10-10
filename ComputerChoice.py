import random
from RockSystem import Rock
from PaperSystem import Paper
from ScissorsSystem import Scissors

def get_computer_choice():
    choices = [Rock, Paper, Scissors]
    return random.choice(choices)()