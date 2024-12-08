import random
from replit import clear
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

def number_result(num1,number):
  if (num1 > number):
    return "Too high"
  elif (num1 < number):
    return "Too low"
  else:
    return "You got it"


def play_game():
  print(logo)
  print("Welcome to Number Guessing game !!")
  print("I am thinking of a number from 1 to 100")
  difficulty = input("Choose a difficulty. type high or low: ")

  if (difficulty == "high"):
    chance = 5
  elif (difficulty == "low"):
    chance = 10
  else:
    chance = 0
  guess = False
  number = random.randint(0, 100)
  while (not guess):
    for _ in range(chance + 1):
      if (chance == 0):
        print("You  lose")
        guess = True
        break
      else:
        print(f"you have {chance} to try guessing the number.")
        chance -= 1
        num1 = int(input("Guess a number: "))
        if (number == num1):
          print("You got it")
          guess = True
          break
        else:
          print(number_result(num1,number))


while (input("Do you want to play the guessing game: ") == "y"):
  clear()
  play_game()
