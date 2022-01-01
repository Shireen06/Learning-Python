# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

def __get_tree(URL):
    source = requests.get(URL)
    seek_jobs = source.text
    soup = BeautifulSoup(seek_jobs, "html.parser")
    return soup
    
def get_all_tags(soup):
    all_tags = soup.find_all(name="div", attrs={"data-search-sol-meta":True})
    for tag in all_tags:
        block_title = tag.find("a")
        title = block_title.string
        print("URL"+block_title["href"])
    
