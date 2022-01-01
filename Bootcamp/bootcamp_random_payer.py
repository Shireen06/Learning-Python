# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:35:10 2021

@author: shiri
"""

# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma.\n ")
names = names_string.split(", ")
#print(names)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#people = len(names)
#choice = random.randint(0, people - 1)
#payer = names[choice]
payer = random.choice(names)
print(payer + " is going to pay today")