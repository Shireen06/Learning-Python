# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:14:48 2021

@author: shiri
"""
#heights: 156 178 165 171 187

student_heights = input("Input a list of student heights ").split()
#print(student_heights)

sum = 0
count = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  sum += student_heights[n]
  count += 1
   
#print(sum)
#print(count)
average = round(sum/count)
print(average)