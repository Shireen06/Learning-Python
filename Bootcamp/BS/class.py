# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 15:44:13 2021

@author: shiri
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd

# class get_jobs (3 param: job name (string), max number of positions(int), name of the file to write to(string))

class job_position:
    def __init__(self, title, link, short_descr, main_points, full_descr):
        self.title = title
        self.link = link
        self.short_description = short_descr
        self.main_points = main_points
        self.full_description = full_descr
    
    def to_dict(self):
        return {'title' : self.title, 'link' : self.link, 'short description' : self.short_description, 'main points' : self.main_points, 'full description' : self.full_description}
        
        
def parse_seek_page(url):
    source = requests.get(url)
    seek_jobs = source.text
    soup = BeautifulSoup(seek_jobs, "html.parser")
    
    jobs = []
    
    all_tags = soup.find_all(name="div", attrs={"data-search-sol-meta":True})
    for tag in all_tags:
        block_title = tag.find("a")
        title = block_title.string
        link = ("https://www.seek.com.au"+block_title["href"])

        lis = tag.find_all(name="li")
        main_points = '\n'.join([li.find("span", class_= "").text for li in lis])
        
        short_descr = tag.find("span", attrs={"data-automation":"jobShortDescription"}).find("span").string

        
        
        descr_full = requests.get(link).text
        descr_soup = BeautifulSoup(descr_full, "html.parser")
        descr_text = descr_soup.find(name="div", attrs={"data-automation":"jobAdDetails"})
        full_description = descr_text.get_text()
        job = job_position(title, link, short_descr, main_points, full_description)
        jobs.append(job)
        
    
    return jobs
    
    
    

def get_seek_jobs(job_name, number_of_positions):
    job_name = job_name.replace(" ", "-")
    template_url = f"https://www.seek.com.au/{job_name}-jobs/?page="
    
    all_jobs = []
    for page_no in range(1, 3):
        page_url = template_url + str(page_no)
        jobs_found = parse_seek_page(page_url)
        if jobs_found is None:
            break
        all_jobs.extend(jobs_found)
    return all_jobs    
    
def save_as_csv(jobs, file_name):
    df = pd.DataFrame([x.to_dict() for x in jobs])
    df.to_csv(file_name, index = False)
    
    
    
results = get_seek_jobs('emberjs', 100)  
save_as_csv(results, 'Jobs_found2.csv')
    
    
    
    
    
    
    
# job_name = input("What type of job you are looking for?")
# number_of_positions = int(input("Please specify the maximum number of positions"))
# file_name = input("Name of the file to save the jobs to")    