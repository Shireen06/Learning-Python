# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:41:26 2021

@author: shiri
"""

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
payment = input("What is the total bill? $ \n")
tips = input("What percentage would you like to leave for a tip? 10, 12, or 15\n")
people = input("How many people are going to share the bill?\n")
bill = int(payment)
tip = (int(tips)/100) * bill
print(tip)
shared = int(people)
chip_in = (bill + tip) / shared
print(round((chip_in), 2))