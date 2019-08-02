# IMDB User Review Scraper

# Currently does the first page (about 25 reviews, need to use something like Selenium for the other reviews)

# Import libraries
from bs4 import BeautifulSoup
from selenium import webdriver 
import requests, sys, webbrowser, bs4
import pandas as pd

# Go To User Review URL and load all the reviews

# browser = webdriver.Firefox()
# browser = webdriver.Firefox(executable_path=r'C:\Program Files\geckodriver\geckodriver.exe')

# browser.get('https://www.imdb.com/title/tt0387898/reviews')

# next_button = browser.find_element_by_id('load-more-trigger')
# type(next_button)

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
        rating = review.findAll('span')[1].contents
        username = review.findAll("a")[1].contents 
        date = review.find("span", {"class": "review-date"}).contents
        text = review.find("div", {"class": "text" }).contents
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

review_data.to_csv('amour_imdb.csv')

