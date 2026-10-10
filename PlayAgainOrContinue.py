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