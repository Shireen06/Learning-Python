# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:38:23 2021

@author: shiri
"""

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
size = size.upper()
add_pepperoni = add_pepperoni.upper()
extra_cheese = extra_cheese.upper()

bill = 0
if size == "S":
  bill = 15
  if add_pepperoni == "Y":
    bill = bill + 2
  if extra_cheese == "Y":
    bill = bill + 1

elif size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill = bill + 3
  if extra_cheese == "Y":
    bill = bill + 1
 
elif size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill = bill + 3
  if extra_cheese == "Y":
    bill = bill + 1

print(f"Your final bill is: ${bill}")









