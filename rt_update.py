from bs4 import BeautifulSoup 
import requests, sys, webbrowser, bs4
import pandas as pd
import openpyxl
import re

# Go To User Review URL and load all the reviews


date_list = []
username_list = []
rating_list = []
text_list = []
useful_list = []

# Number of review pages
# number_reviews = 129

# pagenumber = 1

# for page in range(number_reviews):

url_sub = 'https://www.rottentomatoes.com/m/cache_2005/reviews?type=user'
url = url_sub
r = requests.get(url)
bs = BeautifulSoup(r.text, 'html.parser')

print(bs)

# pagenumber += 1

for review in bs.findAll('li', {'class': 'audience-reviews__item'}):

                # Find username
                username = review.find("a", {"class": 'audience-reviews__name'})
                username = username.text
                
                # find date
                date = review.find("span", {"class": "audience-reviews__duration"}).contents
                
                # Find the text
                review = review.find('p', attrs={'class': 'audience-reviews__review'})
                text  = review.text

                # # find the rating 
                # find_rating = review.find("div", {"class": "scoreWrapper" })
                # string_rating = str(find_rating)
                # rating = re.sub("[^0-9]", "", string_rating)

                # if any(str.isdigit(c) for c in rating) is False:
                #         rating = 'Not Interested' 
                # else:
                #         rating = int(rating) / 10
