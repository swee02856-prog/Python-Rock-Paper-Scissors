import random

def JimmyVoiceLine():
        return random.choice(["Jimmy the Joker: Let's see how you handle my tricks!", "I ain't gonna let that slide PUNK!", "Your Journey ends HERE now!"])
def TimmyVoiceLine():
        return random.choice(["Timmy le destroyer: I'm here to le crush le you.", "You think you can stop me? Nah 1v1 in roblox Rivals!", "Le power of brainrot es me no habla espanol!"])
def BillyVoiceLine():
        return random.choice(["Billy Badass: Holy im so tuff you wilding boii come here.. (Disney Bully Music goes here)", "Ayo 1v1 in BLOX fruits Loser..", "Have you ever played blox fruits but with your LIFE on the line with a bunch of mangos inside of your mouth? heh, dark mango phsychology.."])
def CharacterVoiceline(character_choice):
    if character_choice == "1":
        return JimmyVoiceLine()
    elif character_choice == "2":
        return TimmyVoiceLine()
    elif character_choice == "3":
        return BillyVoiceLine()
    else:
          return["Error: invalid Character Voiceline"]