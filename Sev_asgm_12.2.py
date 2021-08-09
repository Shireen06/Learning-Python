# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 10:53:07 2021

@author: -
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')

count = 0
sum = 0

for tag in tags:
    num = int(tag.contents[0])
    sum = num + sum
    count = count + 1
    

    
print('Count', count, '\nSum', sum)