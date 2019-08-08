from bs4 import BeautifulSoup 
from selenium import webdriver 
from datetime import datetime, timedelta

import requests, sys, webbrowser, bs4
import pandas as pd
import re

# Go To User Review URL and load all the reviews

# film name and URL of user reviews
film_name = input("Enter the title of film: ")
url_input = input("Enter URL of User Reviews: ")

url = url_input
r = requests.get(url)

# Open browser
browser = webdriver.Firefox()
browser.get(url)
    
number_of_reviews = 1000

# Lists of all data 
date_list = []
username_list = []
rating_list = []
text_list = []
useful_list = []
super_list = []

# Loops the entire script 5 times

# Checks the number of times the film has been looped over
loop_number = 0

# for each page of reviews it will loop over each audience review item 
for page in range(number_of_reviews):

    # Get the raw HTML to loop over
    bs = BeautifulSoup(browser.page_source, 'html.parser')

    for review in bs.findAll('li', {'class': 'audience-reviews__item'}):
        number_of_reviews = len(bs.findAll('li', {'class': 'audience-reviews__item'}))

        # Find username
        username = review.find("a", {"class": 'audience-reviews__name'})
        if username is None:
            username = 'No Username'
        else:
            username = username.text


        # find date
        date = review.find("span", {"class": "audience-reviews__duration"})
        date = date.text 

        # Checks to see if review as in the last 7 days or not, formats it correctly
        week = "d ago"

        if week in date:
            days_ago = date.replace("d ago", "")
            days_ago_int = int(days_ago)
            date = datetime.now() - timedelta(days=days_ago_int)
            date = date.strftime('%m/%d/%Y')
            print(date)

        # formats the date
        try:    
            date = date.replace("Jan", "1/")
            date = date.replace("Feb", "2/")
            date = date.replace("Mar", "3/")
            date = date.replace("Apr", "4/")
            date = date.replace("May", "5/")
            date = date.replace("Jun", "6/")
            date = date.replace("Jul", "7/")
            date = date.replace("Aug", "8/")
            date = date.replace("Sep", "9/")
            date = date.replace("Oct", "10/")
            date = date.replace("Nov", "11/")
            date = date.replace("Dec", "12/")
        except:
            date = 'No Date'

        date = date.replace(",", "/")
        date = date.replace(" ", "")

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

        # Finds out if user is Super Reviewer
        super_user = review.find("strong", {"class": "super-reviewer-badge" })

        if super_user is None:
            super_user = 'No'
        else:
            super_user = 'Yes'

        # add each item to the lists
        super_list.append(super_user)
        date_list.append(date)
        username_list.append(username)
        rating_list.append(rating)
        text_list.append(text)
    
    # tries to find the NEXT button and click it, if it can't it will do an entire film loop again until the loop number reaches 3.
    try:
        button = browser.find_element_by_css_selector('nav.prev-next-paging__wrapper:nth-child(3) > button:nth-child(2) > span:nth-child(1)')
        button.click()
        browser.delete_all_cookies()
    except:
        loop_number += 1
        print(loop_number)
        # break once we loop 5 times
        # change this number if want to increase/decrease number of times the film is looped over.
        if loop_number == 5:
            break
        else:
            browser.get(url)


#Create dataframe
review_data = pd.DataFrame(
    {
     'Username': username_list,
     'Super Reviewer': super_list,
     'Date': date_list,
     'Rating (out of 5)': rating_list,
     'Review Text': text_list,
     }
)

# Add a notes column
review_data['Notes'] = ''

# Converts Date column to datetime format, then turns into European date style
review_data['Date'] =  pd.to_datetime(review_data['Date'], format='%m/%d/%Y')
review_data['Date'] = review_data['Date'].dt.strftime('%d/%m/%Y')

# Gets rid of all duplicates
review_data = review_data.drop_duplicates()

# Create data file
review_data.to_csv(film_name + '_rt.csv')
