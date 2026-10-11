import random

def JimmyVoiceLine():
        return random.choice(["Jimmy the Joker: Let's see how you handle my tricks!", "Jimmy the Joker: I ain't gonna let that slide PUNK!", "Jimmy the Joker: Your Journey ends HERE now!"])
def TimmyVoiceLine():
        return random.choice(["Timmy le destroyer: I'm here to le crush le you.", "Timmy le destroyer: You think you can stop me? Nah 1v1 in roblox Rivals!", "Timmy le destroyer: Le power of brainrot es me no habla espanol!"])
def BillyVoiceLine():
        return random.choice(["Billy Badass: Holy im so tuff you wilding boii come here.. (Disney Bully Music goes here)", "Billy Badass: Ayo 1v1 in BLOX fruits Loser..", "Billy Badass: Have you ever played blox fruits but with your LIFE on the line with a bunch of mangos inside of your mouth? heh, dark mango phsychology.."])
def CharacterVoiceline(character_choice):
    if character_choice == "1":
        return JimmyVoiceLine()
    elif character_choice == "2":
        return TimmyVoiceLine()
    elif character_choice == "3":
        return BillyVoiceLine()
    else:
          return["Error: invalid Character Voiceline"]

def JimmyGreeting():
        return random.choice(["Jimmy the Joker: I've battled lots of opponents before! Lets see how this goes..", "Jimmy the Joker: Ready for a challenge?", "Jimmy the Joker: Bring it on!"])
def TimmyGreeting():
        return random.choice(["Timmy le destroyer: You Only Live Once, But Ig rn its thrice.", "Timmy le destroyer: You think you can beat me? Bring it on!", "Timmy le destroyer: Bro I wanna play Chess not this bs.."])
def BillyGreeting():
        return random.choice(["Billy Badass: You done now boii.. (Inner mangoness kicks in)", "Billy Badass: YOU THINK YOUR THE KING? NAH IM THE KING BOI", "Billy Badass: Welcome to BP brother (Demon Ronaldo)"])

def CharacterGreeting(character_choice):
    if character_choice == "1":
        return JimmyGreeting()
    elif character_choice == "2":
        return TimmyGreeting()
    elif character_choice == "3":
        return BillyGreeting()
    else:
          return["Error: invalid Character Greeting"]