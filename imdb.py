# IMDB User Review Scraper

# Import libraries
from bs4 import BeautifulSoup
from selenium import webdriver 
import requests, sys, webbrowser, bs4
import pandas as pd

# film_name = input("Enter the title of film: ")
# url_input = input("Enter URL of User Reviews: ")

# url_sub = url_input
url = 'https://www.imdb.com/title/tt1602620/reviews?ref_=tt_ov_rt'
r = requests.get(url)

browser = webdriver.Firefox()
browser.get(url)

number_of_reviews = 1000

title_list = []
rating_list = []
username_list = []
date_list = []
text_list = []
useful_list = []

for page in range(number_of_reviews):
    try:
        button = browser.find_element_by_class_name('ipl-load-more__button')
        button.click()
    except:
        print('Exception')

bs = BeautifulSoup(browser.page_source, 'html.parser')

for review in bs.findAll('div', {'class': 'review-container'}):
        # rating = review.findAll('span', {'class' : 'rating-other-user-rating'}) 
        # user_rating = rating.span[2].contents
        title = review.a.contents
        title = ''.join(title)


        date = review.find("span", {"class": "review-date"}).contents
        rating = str(review.findAll('span')[1].contents)

        print(date)
        print(rating)

        if date is rating:
            print('SAME')
        else:
            rating = rating[2:4]
  


        date = ''.join(date)

        print


        username = review.findAll("a")[1].contents
        username = ''.join(username)
        
        text = review.find("div", {"class": "text" }).contents
        text = str(text)

        useful = review.select('div.actions.text-muted') 

        title_list.append(title)
        rating_list.append(rating)
        username_list.append(username)
        date_list.append(date)
        text_list.append(text)
        useful_list.append(useful)  

# Create dataframe
review_data = pd.DataFrame(
    {'Title': title_list,
     'Rating (out of 10)': rating_list,
     'Username': username_list,
     'Date': date_list,
     'Review Text': text_list,
     'Usefulness': useful_list,
     }
)

review_data.to_csv('filmname_imdb.csv')

