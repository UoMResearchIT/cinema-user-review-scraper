# IMDB User Review Scraper

# Import libraries
from bs4 import BeautifulSoup
from selenium import webdriver 
import requests, sys, webbrowser, bs4
import pandas as pd
import re



# User inputs name of film and URL of user reviews
film_name = input("Enter the title of film: ")
url_input = input("Enter URL of User Reviews: ")

url = url_input
r = requests.get(url)

# Starts browser and navigates to appropiate page
browser = webdriver.Firefox()
browser.get(url)

# arbitarily large number of reviews
number_of_reviews = 1000

# Lists where all the scraped data will go into. 
title_list = []
rating_list = []
username_list = []
date_list = []
text_list = []
useful_list = []
useful_total_list = []


# Loop that clicks the load more button until it can no longer do so.
for page in range(number_of_reviews):
    try:
        button = browser.find_element_by_class_name('ipl-load-more__button')
        button.click()
    except:
        continue

# Gets HTML of page with ALL user reviews
bs = BeautifulSoup(browser.page_source, 'html.parser')

useful_loop_count = 0

# Loops over each review on the page with all user reviews
for review in bs.findAll('div', {'class': 'review-container'}):

        # Gets title of review
        title = review.a.contents
        try:
            title = ''.join(title)
        except:
            title = "No Title Given"


        # Checks to see if a rating was given. Sometimes there's none given.
        date = str(review.find("span", {"class": "review-date"}).contents)
        rating = str(review.findAll('span')[1].contents)

        if date == rating:
            rating = "No Rating given"
        else:
            rating = review.findAll('span')[1].contents
            rating = ''.join(rating)
        
        # Get Date
        date = review.find("span", {"class": "review-date"}).contents
        date = ''.join(date)

        # Formats the date into numerical format
        try:    
            date = date.replace("January", "/1/")
            date = date.replace("February", "/2/")
            date = date.replace("March", "/3/")
            date = date.replace("April", "/4/")
            date = date.replace("May", "/5/")
            date = date.replace("June", "/6/")
            date = date.replace("July", "/7/")
            date = date.replace("August", "/8/")
            date = date.replace("September", "/9/")
            date = date.replace("October", "/10/")
            date = date.replace("November", "/11/")
            date = date.replace("December", "/12/")
        
        except:
            date = 'No Date'

        date = date.replace(" ", "")

        # Username
        username = review.findAll("a")[1].contents
        username = ''.join(username)
        

        # Text of Review
        text = review.find("div", {"class": "text" })
        text = text.text


        # Usefullness of Review
        # Gets the tag then strips all text to leave numbers which are then put into two different columns
        useful = bs.findAll("div", attrs={"class": "actions text-muted"})[useful_loop_count]
        useful = useful.text
        useful = useful.replace("Was this review helpful?  Sign in to vote.", "")
        useful = useful.replace("Permalink", "")
        useful = str(useful)
        
        stripped = re.findall(r"\b\d+\b", useful)

        useful = stripped[0]
        useful_total = stripped[1]

        useful_loop_count += 1

        # scraped data of review is added to the lists
        title_list.append(title)
        rating_list.append(rating)
        username_list.append(username)
        date_list.append(date)
        text_list.append(text)
        useful_list.append(useful)
        useful_total_list.append(useful_total)  

# Create dataframe, with following columns
review_data = pd.DataFrame(
    {
        'Username': username_list,
        'Date': date_list,
        'Title': title_list,
        'Rating (out of 10)': rating_list,
        'Review Text': text_list,
        'No. Found Review Useful': useful_list,
        'Usefulness Total': useful_total_list,
     }
)

# Create Notes column
review_data['Notes'] = ''

# Format date column to datetime format
review_data['Date'] =  pd.to_datetime(review_data['Date'], format='%d/%m/%Y')

# Change date format to European order
review_data['Date'] = review_data['Date'].dt.strftime('%d/%m/%Y')

# Create CSV with the all the user review data
review_data.to_csv(film_name + '_imdb.csv')

