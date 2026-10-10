from RockSystem import Rock
from PaperSystem import Paper
from ScissorsSystem import Scissors
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