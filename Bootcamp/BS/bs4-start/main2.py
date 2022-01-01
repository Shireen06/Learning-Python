# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

responce = requests.get("https://news.ycombinator.com/")
yc_page = responce.text

soup = BeautifulSoup(yc_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink" )
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
    
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]



# print(article_upvotes)

largest_number = max(article_upvotes) 
largest_index = article_upvotes.index(largest_number)
print(largest_index)
print(article_texts[largest_index])
print(article_links[largest_index])



#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# links = soup.find(name="a href")
# print(links)
# jobs_urls = soup.select_one(selector="#jobTitle")
# heading = soup.select(".heading")
# print(heading)
#print(jobs_urls)


# heading = soup.find(href="/data-scientist")
# print(heading)



# with open("website.html", encoding='utf-8') as file:
#     contents = file.read()
    
# soup = BeautifulSoup(contents, "html.parser")
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# if page >1:
#         next_page = page + 1
# print(next_page)