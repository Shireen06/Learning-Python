# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:13:58 2021

@author: shiri
"""

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

import random

game_images = [rock, paper, scissors]

choice1 = int(input("Type in your number. 0 is rock, 1 is paper, and 2 is scissors \n"))
if choice1 >= 3 or choice1 < 0:
  print("You typed invalid number. You lose!")
else:
  print(game_images[choice1])

  choice2 = random.randint(0,2)
  print("Computer chose: ")
  print(game_images[choice2])

  #rock = 0
  #paper = 1
  #scissors = 2
  if choice1 == 0 and choice2 == 2:
    print("You win!")
  elif choice2 == 0 and choice1 == 2:
    print("You lose!")
  elif choice2 > choice1:
    print("You lose!")
  elif choice1 > choice2:
    print("You win!")
  elif choice2 ==  choice1:
    print("tie!")



