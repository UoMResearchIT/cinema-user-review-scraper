# Allo Cine User Review Scraper

# Currently does the first page (about 25 reviews, can loop over the URL later to get all the reviews, still need to exctract text and usefulness)

# Import libraries
from bs4 import BeautifulSoup 
import requests, sys, webbrowser, bs4
import pandas as pd
import openpyxl
import json
import re

# Go To User Review URL and load all the reviews

date_list = []
username_list = []
rating_list = []
text_list = []
useful_list = []

loop_count = 0
pagenumber = 1

number_reviews = 31

for page in range(number_reviews):


    url = 'http://www.allocine.fr/film/fichefilm-43921/critiques/spectateurs/?page=%s' % pagenumber
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')

    pagenumber += 1

    loop_count = 0


    for review in bs.findAll('div', {'class': 'hred review-card cf'}):
    
        # Rating
        rating = review.find("span", {"class": "stareval-note"}).contents
        
        # Username
        username = review.findAll("span")[1].contents

        # Date
        date = review.find("span", {"class": "review-card-meta-date light" })
        date_text = date.text
        date_text_strip = re.sub("[^0-9/]", "", date_text)

        # Review Text
        review_text = bs.findAll("div", attrs={"class": "content-txt review-card-content"})[loop_count]
        text = review_text.text
        loop_count += 1

        # Followers    
        # new_soup = review.text
        # followers = new_soup.findAll(text="abonnés")


        # Number of Reviews

        # Usefulness    
        date_list.append(date_text_strip)
        username_list.append(username)
        rating_list.append(rating)
        text_list.append(text)
    

# Create dataframe
review_data = pd.DataFrame(
    {
     'Date': date_list,
     'Username': username_list,
     'Rating (out of 5)': rating_list,
     'Review Text': text_list,
     }
)

# review_data['Date'] = pd.to_datetime(review_data.Date)

# review_data.sort_values(by='Date')

review_data.to_csv('ac_review_data.csv')
review_data.to_excel('ac_review_data.xlsx')

