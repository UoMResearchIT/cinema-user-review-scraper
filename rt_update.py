from bs4 import BeautifulSoup 
from selenium import webdriver 

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

url_sub = 'https://www.rottentomatoes.com/m/cache_2005/reviews/?page=%s&type=user&sort='
url = url_sub
r = requests.get(url)
bs = BeautifulSoup(r.text, 'html.parser')

# print(bs)

review_number = 0 
total_page_number = 0

for review in bs.findAll('li', {'class': 'audience-reviews__item'}):
    
    number_of_reviews = len(bs.findAll('li', {'class': 'audience-reviews__item'}))

    # Find username
    username = review.find("a", {"class": 'audience-reviews__name'})
    username = username.text
    
    # find date
    date = review.find("span", {"class": "audience-reviews__duration"})
    date = date.text 
    
    # Find the text
    review_text = review.find('p', attrs={'class': 'audience-reviews__review'})
    text  = review_text.text

    # find the rating 
    find_rating_filled = review.findAll("span", {"class": "star-display__filled" })
    find_rating_half = review.findAll("span", {"class": "star-display__half" })

    full_star = len(review.findAll("span", {"class": "star-display__filled" }))
    half_star = len(review.findAll("span", {"class": "star-display__half" }))

    if half_star > 0:
        half_star = 0.5
    else:
        half_star = 0

    rating = full_star + half_star

    # Is a superuser?

    date_list.append(date)
    username_list.append(username)
    rating_list.append(rating)
    text_list.append(text)

    review_number += 1

    if review_number == number_of_reviews:
        
        total_page_number += 1
        
        browser = webdriver.Firefox()
        browser.get(url)
        
        for page in range(total_page_number):
            button = browser.find_element_by_css_selector('nav.prev-next-paging__wrapper:nth-child(3) > button:nth-child(2) > span:nth-child(1)')
            button.click()
            browser.delete_all_cookies()
            button = browser.find_element_by_css_selector('nav.prev-next-paging__wrapper:nth-child(3) > button:nth-child(2) > span:nth-child(1)')
            button.click() 
            

        

# Create dataframe
review_data = pd.DataFrame(
    {
     'Date': date_list,
     'Username': username_list,
     'Rating (out of 5)': rating_list,
     'Review Text': text_list,
     }
)

review_data.sort_values(by=['Date'])

review_data.to_csv('rt_user_reviews.csv')