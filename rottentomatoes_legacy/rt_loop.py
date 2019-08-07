from bs4 import BeautifulSoup 
from selenium import webdriver 

import requests, sys, webbrowser, bs4
import pandas as pd
import re

# Go To User Review URL and load all the reviews

url_sub = 'https://www.rottentomatoes.com/m/cache_2005/reviews/?page=%s&type=user&sort='
url = url_sub
r = requests.get(url)

browser = webdriver.Firefox()
browser.get(url)
    
loop_count = 0
pagenumber = 1

number_of_reviews = 300

date_list = []
username_list = []
rating_list = []
text_list = []
useful_list = []


for page in range(number_of_reviews):
    
    bs = BeautifulSoup(browser.page_source, 'html.parser')

    for review in bs.findAll('li', {'class': 'audience-reviews__item'}):
        number_of_reviews = len(bs.findAll('li', {'class': 'audience-reviews__item'}))

        # Find username
        username = review.find("a", {"class": 'audience-reviews__name'})
        print(username)
        if username is None:
            username = 'No Username'
        else:
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
    
    try:
        button = browser.find_element_by_css_selector('nav.prev-next-paging__wrapper:nth-child(3) > button:nth-child(2) > span:nth-child(1)')
        button.click()
        browser.delete_all_cookies()
    except:
        break        
        
#Create dataframe
review_data = pd.DataFrame(
    {
     'Date': date_list,
     'Username': username_list,
     'Rating (out of 5)': rating_list,
     'Review Text': text_list,
     }
)

# review_data.sort_values(by=['Date'])

review_data.to_csv('rt_user_reviews.csv')


# IGNORE ALL THIS

# button.click()
# browser.delete_all_cookies()

# file = open('pagetwo.txt','w') 
# file.write(browser.page_source) 
# file.close()

# button = browser.find_element_by_css_selector('nav.prev-next-paging__wrapper:nth-child(3) > button:nth-child(2) > span:nth-child(1)')
# button.click()
# browser.delete_all_cookies()

# button = browser.find_element_by_css_selector('nav.prev-next-paging__wrapper:nth-child(3) > button:nth-child(2) > span:nth-child(1)')
# button.click()
# browser.delete_all_cookies()

# file = open('pagefour.txt','w') 
# file.write(browser.page_source) 
# file.close()


# button = browser.find_element_by_css_selector('nav.prev-next-paging__wrapper:nth-child(3) > button:nth-child(2) > span:nth-child(1)')
# button.click()
# browser.delete_all_cookies()
# browser.page_source
# print(browser.page_source)

# file = open('pagefive.txt','w') 
# file.write(browser.page_source) 
# file.close()

# button = browser.find_element_by_css_selector('nav.prev-next-paging__wrapper:nth-child(3) > button:nth-child(2) > span:nth-child(1)')
# button.click()
# browser.delete_all_cookies()
# browser.page_source
# print(browser.page_source)

# file = open('pagesix.txt','w') 
# file.write(browser.page_source) 
# file.close()