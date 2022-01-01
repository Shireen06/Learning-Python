# Job title
# Company name (employer)
# Location 1 (eg.Sydney)
# Location 2 (eg. CBD)
# Salary
# Position type
# Job link
# Short description
# Full descr. raw
# Full descr. txt
# When posted(?)

# -*- coding: utf-8 -*-



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
    # print(title)
    # print(link)
    lis = tag.find_all(name="li")
    for li in lis:
        bullet = li.find("span", class_= "")
        #print(bullet.string)
    short_descr = tag.find("span", attrs={"data-automation":"jobShortDescription"}).find("span").string
    # print(short_descr)
    # print("\n")
    
    descr_full = requests.get(link).text
    descr_soup = BeautifulSoup(descr_full, "html.parser")
    descr_text = descr_soup.find(name="div", attrs={"data-automation":"jobAdDetails"}).find_all()
    descr_text_pr = "\n".join(map(lambda t: t.string or "", descr_text))
    post = descr_soup.find(name="span", attrs={"data-automation":"jobListingDate"}).find_all()
    print(post) 
    
    # data = pd.DataFrame(columns=[{'Title': [title], 'Link': [link], 'Short_descr': [short_descr], 'Full_descr': [descr_text_pr]}])
    # for title, link, short_descr, descr_text_pr in zip(data['Title'], ['link'], ['Short_descr'], ['Full_descr']):
    #     print(title, link, short_descr, descr_text_pr)
    
    # for title in block_title:
    #     temp_df = pd.DataFrame([title], columns=['Title'])
    #     data = data.append(temp_df, ignore_index=True)
    # for descr in short_descr:
    #     temp_df = pd.DataFrame([short_descr], columns=['Short_descr'])
    #     data = data.append(temp_df, ignore_index=True)
    # for Full_descr in descr_text_pr:
    #     temp_df = pd.DataFrame([descr_text_pr], columns=['Full_descr'])
    #     data = data.append(temp_df, ignore_index=True)
        
   
    
    
    # with open("scraping_outcome.txt", "a") as file:
    #     file.write(str(data))

    # df = pd.read_csv(r"scraping_outcome.txt", encoding='windows-1252', sep="\n")
    # df.to_csv(r"C:\Dev\Learning-Python\Bootcamp\scraping_outcome.csv", index=None)     
 

