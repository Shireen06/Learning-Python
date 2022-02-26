#Number Guessing Game Objectives:
from art import logo
print(logo)
import random

#print(logo)
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
easy_level = 10
hard_level = 5
def guess_check(real_number,guess,turns):
  if guess > real_number:
    print("Too high")
    return turns - 1
  elif guess < real_number:
    print("Too low!")
    return turns - 1
  else:
    print(f"Bingo! The answer was {real_number}")

def difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return easy_level
  else:
    return hard_level


def play_game():
  print("Welcome to the guess the number game!")
  numbers = range(1, 101)
  real_number = random.choice(numbers)
  #print(real_number)
  turns = difficulty()
  
  guess = 0
  while guess != real_number:
    print(f"You have {turns} attempts left")
    guess = int(input("Type a number between 1 and 100: "))
    turns = guess_check(real_number, guess, turns)
    if turns == 0:
      print("You run out of guesses")
      return

play_game()







