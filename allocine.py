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
user_details_list = []
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
        rating = str(review.find("span", {"class": "stareval-note"}).contents)
        
        # Username
        username = str(review.findAll("span")[1].contents)

        # User details
        try:
                user_details = str(review.find("p", {"class": "meta-content light"}).contents)
                user_details = re.sub("<span.*>", "", user_details)
                user_details = re.sub("</span>", "", user_details)
                user_details = re.sub("'\\n'", "", user_details)
                user_details = user_details.replace("'\\n'", "")
                user_details = user_details.replace(",", "")
                user_details = user_details.replace("[", "")
                user_details = user_details.replace("]", "")
                user_details = user_details.replace("Suivre son activité", "")
                user_details = user_details.strip()

        except:
                user_details = 'No User Details'


        # Date
        # date = review.find("span", {"class": "review-card-meta-date light" })
        # date_text = date.text
        # date_text_strip = re.sub("[^0-9/]", "", date_text)

        # Review Text
        review_text = bs.findAll("div", attrs={"class": "content-txt review-card-content"})[loop_count]
        text = review_text.text
        loop_count += 1

        # Usefulness 
        usefulness = bs.findAll("div", {"class": "review-card-social"})
        print(usefulness)

        # Add to list
        username_list.append(username)
        rating_list.append(rating)
        text_list.append(text)
        user_details_list.append(user_details)
    

# Create dataframe
review_data = pd.DataFrame(
    {
     'Username': username_list,
     'User Details': user_details_list,
     'Rating (out of 5)': rating_list,
     'Review Text': text_list,
     }
)

# review_data['Date'] = pd.to_datetime(review_data.Date)

# review_data.sort_values(by='Date')

#JSOn data co to CSV

review_data.to_csv('ac_review_data.csv')

