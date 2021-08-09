# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 12:16:22 2021

@author: -
"""
import re
name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_42.txt"
handle = open(name)
numlist = list()
for line in handle:
    line = line.rstrip()
   
    nums = re.findall('[0-9]+', line)
   
    if len(nums) == 0 :
        continue
  
    for num in nums:
        numlist.append(int(num))
   
print(sum(numlist))


