# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:51:06 2021

@author: shiri
"""

#78 65 89 86 55 91 64 89

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  #print(student_scores)

largest_number = -1
for number in student_scores:
  if number > largest_number:
    largest_number = number
print(f"The highest score in the class is: {largest_number}")