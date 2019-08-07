# Rotten Tomatoes User Review Scraper

# Import libraries
from bs4 import BeautifulSoup 
import requests, sys, webbrowser, bs4
import pandas as pd
import re

# Go To User Review URL and load all the reviews


date_list = []
username_list = []
rating_list = []
text_list = []
useful_list = []

# Number of review pages
number_reviews = 129

pagenumber = 1

for page in range(number_reviews):

        url_sub = 'https://www.rottentomatoes.com/m/cache_2005/reviews/?page=%s&type=user&sort=' % pagenumber
        url = url_sub
        r = requests.get(url)
        bs = BeautifulSoup(r.text, 'html.parser')

        print(bs)

        pagenumber += 1


        for review in bs.findAll('div', {'class': 'row review_table_row'}):

                rating = review.findAll('span')[1].contents
                username = review.find("span", {"style": "word-wrap:break-word"}).contents
                date = review.find("span", {"class": "fr small subtle"}).contents
                
                #find the text
                review = review.find('div', attrs={'class': 'user_review'})
                text  = review.text
                
                # find the rating 
                find_rating = review.find("div", {"class": "scoreWrapper" })
                string_rating = str(find_rating)
                rating = re.sub("[^0-9]", "", string_rating)

                if any(str.isdigit(c) for c in rating) is False:
                        rating = 'Not Interested' 
                else:
                        rating = int(rating) / 10

                # Find Super Reviewer
                # find_super_reviewer = review.find('div', attrs={'style': 'color:#FFAE00'})
                # superreview = find_super_reviewer.text
                # print(superreview)

                date_list.append(date)
                username_list.append(username)
                rating_list.append(rating)
                text_list.append(text)



# Create dataframe
review_data = pd.DataFrame(
    {
     'Date': date_list,
     'Username': username_list,
     'Rating (out of 10)': rating_list,
     'Review Text': text_list,
     }
)

review_data.sort_values(by=['Date'])

review_data.to_csv('rt_user_reviews.csv')
review_data.to_excel('rt_user_reviews.xlsx')

