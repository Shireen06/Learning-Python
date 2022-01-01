# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:36:30 2021

@author: shiri
"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You are at a crossroad. Which way would you like to go left or right? Type r or l \n")

choice = direction.lower()
r = "r"
l = "l"
if choice == r:
  print("You fell from a cliff. Game over")
  exit()
else:
  print("You are on a shore of a lake")

next_step = input("The treausre is on an island in the middle of the lake. Would you like to wait for a boat or swim? Type w or s \n")
lowercase = next_step.lower()
s = "s"
w = "w"
if lowercase == w:
  print("You are on the island.")
else:
  print("Game over, you were eaten by a shark")
  exit()

last_step = input("There is a building with three doors - red, green, and yellow. The treasure is behind one of them. Choose your door. Type R, G, or Y \n")
final = last_step.lower()
r = "r"
g = "g"
y = "y"
if final == y:
  print("You found the treasure, you won the game!")
else:
  print("Game over, you chose the wrong door!")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload