# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import csv

source = requests.get("https://www.seek.com.au/data-scientist-jobs/in-All-Sydney-NSW?page=1")
seek_jobs = source.text


with open('Scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    for pagecounter in range(3):
        soup = BeautifulSoup(seek_jobs, "html.parser")
        all_tags = soup.find_all(name="div", attrs={"data-search-sol-meta":True})
        for tag in all_tags:
            block_title = tag.find("a")
            title = block_title.string
            link = ("https://www.seek.com.au"+block_title["href"])
            writer.writerow(title)
            writer.writerow(link)
            print(title)
            print(link)
        
            lis = tag.find_all(name="li")
            for li in lis:
                bullet = li.find("span", class_= "")
        short_descr = tag.find("span", attrs={"data-automation":"jobShortDescription"}).find("span").string
        writer.writerow(short_descr)
        print(short_descr)
        print("\n")
       
            descr_full = requests.get(link).text
            descr_soup = BeautifulSoup(descr_full, "html.parser")
            print(descr_soup)
            descr_text = descr_soup.find(name="div", attrs={"data-automation":"jobAdDetails"})
            full = descr_text.get_text()
            writer.writerow(full)
            print(full)
            print(pagecounter + 1)
            print("\n")
            
        if pagecounter == 1:
                nextLink = soup.select('a[data-offset]')[0]
        elif pagecounter != 1:
                nextLink = soup.select('a[data-offset]')[1]