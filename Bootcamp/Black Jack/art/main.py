import os 
os.system('cls')
import random
from art import logo
print(logo)

def deal_card():
#11 is the Ace.
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
deal_card()

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  elif 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)  
  return sum(cards)

def compare(user, computer):
  if user == computer:
    return "Draw"
  elif computer == 0:
    return "Computer has black jack! Computer won"
  elif user == 0 and computer != 0:
    return "You have a black jack! You won"
  elif user > 21:
    return "You are over 21, you lose"
  elif computer > 21:
    return "Computer went over, you win"
  elif user > computer:
    return "You won"
  else:
    return "You lose"

def play_game():
  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user = calculate_score(user_cards)
    computer = calculate_score(computer_cards)
    print(f" Your cards: {user_cards}, current score: {user}")
    print(f" Computer's first card: {computer_cards[0]}")

    if user == 0 or computer == 0 or user > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y'to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer != 0 and computer < 17:
    computer_cards.append(deal_card())
    computer = calculate_score(computer_cards)
  print(f" Your final score is: {user}, computer's cards are: {computer_cards}, computer's final score is: {computer}")
  print(compare(user, computer))

while input("Would you like to play another round? Type 'y' or 'n': ") == "y":
      'cls'
      play_game()

