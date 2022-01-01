# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:39:35 2021

@author: shiri
"""

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
Weight = float(weight)
#print(Weight)
Height = float(height)
#print(Height)
BMI = round((Weight)/(Height)**2)
#print(BMI)
if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight")
elif BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight")
elif BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight")
elif BMI < 35:
  print(f"Your BMI is {BMI}, you are obese")
else:
  print(f"Your BMI is {BMI}, you are clinically obese")