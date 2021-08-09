# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 15:40:24 2021

@author: -
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

while count >= 0 :
    print('Retrieving: ', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[position - 1]
    url = link.get('href', None)
    count = count - 1

    

    
