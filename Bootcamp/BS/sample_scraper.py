from bs4 import BeautifulSoup
import requests
import pandas as pd


source = requests.get("https://www.seek.com.au/data-scientist-jobs/in-All-Sydney-NSW?page=1")
seek_jobs = source.text
soup = BeautifulSoup(seek_jobs, "html.parser")
   


all_tags = soup.find_all(name="div", attrs={"data-search-sol-meta":True})
for tag in all_tags:
    block_title = tag.find("a")
    title = block_title.string
    link = ("https://www.seek.com.au"+block_title["href"])
    print(title)
    print(link)
    lis = tag.find_all(name="li")
    for li in lis:
        bullet = li.find("span", class_= "")
        print(bullet.string)
    short_descr = tag.find("span", attrs={"data-automation":"jobShortDescription"}).find("span").string
    print(short_descr)
    print("\n")
    
    descr_full = requests.get(link).text
    descr_soup = BeautifulSoup(descr_full, "html.parser")
    descr_text = descr_soup.find(name="div", attrs={"data-automation":"jobAdDetails"})
    full = descr_text.get_text()
    print(full)
    print("\n")
    

    
    

 # body = descr_text.select_one(selector="p strong")
 # print(body) 