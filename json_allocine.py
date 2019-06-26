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

review_json = []

loop_count = 0
pagenumber = 11

number_reviews =  3

for page in range(number_reviews):


    url = 'http://www.allocine.fr/film/fichefilm-43921/critiques/spectateurs/?page=%s' % pagenumber
    print(url)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')

    print(bs)

    review = bs.find("script", {"type": "application/ld+json"})

    review_json.append(review)

    pagenumber += 1

    loop_count = 0

# print(review_json)

# Create dataframe
# review_data = pd.DataFrame(
#     {
#      'Date': date_list,
#      'Username': username_list,
#      'Rating (out of 5)': rating_list,
#      'Review Text': text_list,
#      }
# )


# review_data.to_csv('ac_review_data.csv')

