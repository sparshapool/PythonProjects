import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
yourchoice = int(
    input("What do you choose? enter 1 for rock,2 for paper,3 for scissors: "))
computerchoice = random.randint(0, 2)
options = ["rock", "paper", "scissors"]
yourchoice = options[yourchoice - 1]
computerchoice = options[computerchoice - 1]
print(f"your choice is {yourchoice}")
if (yourchoice == "paper"):
  print(paper)
elif (yourchoice == "rock"):
  print(rock)
else:
  print(scissors)
print(f"computer choice is {computerchoice}")
if (computerchoice == "paper"):
  print(paper)
elif (computerchoice == "rock"):
  print(rock)
else:
  print(scissors)

if (yourchoice == "rock" and computerchoice == "sissors"):
  print("You win")
elif (yourchoice == "paper" and computerchoice == "rock"):
  print("You win")
elif (yourchoice == "scissors" and computerchoice == "paper"):
  print("you win")
elif (yourchoice == computerchoice):
  print("draw")
else:
  print("computer wins")
