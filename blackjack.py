import random
from replit import clear

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
    return sum(cards)
  return sum(cards)


def compare(user_score, computer_score):
  if (user_score == computer_score):
    return ("Draw")
  elif (computer_score == 0):
    return ("You loose, opponent has blackjack")
  elif (user_score == 0):
    return ("You win with a blackjack")
  elif (user_score > 21):
    return ("You went over, you loose")
  elif (computer_score > 21):
    return ("Opponent went over, you win")
  elif (computer_score > user_score):
    return ("Computer wins")
  else:
    return ("User wins")


def play_game():

  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)

  while (not is_game_over):
    print(f"Your cards: {user_cards},current score: {user_score}")
    print(f"Computers first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
      print(f"Your final cards: {user_cards},Your final score: {user_score}")
      print(f"Computers final score: {computer_cards[0]}")
      print("You lose!")
    else:
      choice = input("Type 'y' to get another card, type 'n' to pass: ")
      if choice == "y":
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
      else:
        while computer_score != 0 and computer_score < 17:
          computer_cards.append(deal_card())
          computer_score = calculate_score(computer_cards)
        is_game_over = True
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(
            f"Computer's final hand: {computer_cards}, final score: {computer_score}"
        )
        print(compare(user_score, computer_score))


while input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
