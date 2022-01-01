# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:42:54 2021

@author: shiri
"""

age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_left = 90 - int(age)
days = years_left * 365
months = years_left * 12
weeks = years_left * 52
 
print (f"You have {days} days, {weeks} weeks, and {months} months left.")