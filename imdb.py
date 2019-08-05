# IMDB User Review Scraper

# Import libraries
from bs4 import BeautifulSoup
from selenium import webdriver 
import requests, sys, webbrowser, bs4
import pandas as pd
import re

film_name = input("Enter the title of film: ")
url_input = input("Enter URL of User Reviews: ")

url = url_input
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

permalink_loop_count = 0
useful_loop_count = 0

for review in bs.findAll('div', {'class': 'review-container'}):
        # rating = review.findAll('span', {'class' : 'rating-other-user-rating'}) 
        # user_rating = rating.span[2].contents
        title = review.a.contents
        title = ''.join(title)

        date = str(review.find("span", {"class": "review-date"}).contents)
        rating = str(review.findAll('span')[1].contents)

        # print(date)
        # print(rating)

        if date == rating:
            rating = "No Rating given"
        else:
            rating = review.findAll('span')[1].contents
            rating = ''.join(rating)
        
        # Get Date
        date = review.find("span", {"class": "review-date"}).contents
        date = ''.join(date)

        try:    
            date = date.replace("January", "1")
            date = date.replace("February", "2")
            date = date.replace("March", "3")
            date = date.replace("April", "4")
            date = date.replace("May", "5")
            date = date.replace("June", "6")
            date = date.replace("July", "7")
            date = date.replace("August", "8")
            date = date.replace("September", "9")
            date = date.replace("October", "10")
            date = date.replace("November", "11")
            date = date.replace("December", "12")
        
        except:
            date = 'No Date'


        # Username
        username = review.findAll("a")[1].contents
        username = ''.join(username)
        

        # Text of Review
        text = review.find("div", {"class": "text" })
        text = text.text


        # Usefullness of Review
        useful = bs.findAll("div", attrs={"class": "actions text-muted"})[useful_loop_count]
        useful = useful.text
        useful = useful.replace("Was this review helpful?  Sign in to vote.", "")
        useful = useful.replace("Permalink", "")
        useful_loop_count += 1


        # Permalink 
        # permalink = bs.findAll("a", attrs={"href": re.compile("/review/")})[permalink_loop_count]        
        # permalink = str(permalink)
        # permalink_loop_count += 1
        # print(permalink)
        # link = re.findall(r"\/review\/rw\d\d\d\d\d\d\d\/\?ref_=tt_urv|$", permalink)
        # link = ''.join(link)
        # imdb_url = "https://www.imdb.com"
        # review_link = imdb_url + link
        # print(review_link)

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

review_data.to_csv(film_name + '_imdb.csv')

