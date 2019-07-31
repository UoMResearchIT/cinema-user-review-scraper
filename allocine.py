# Allo Cine User Review Scraper

# Currently does the first page (about 25 reviews, can loop over the URL later to get all the reviews, still need to exctract text and usefulness)

# Import libraries
from bs4 import BeautifulSoup 
import requests, sys, webbrowser, bs4
import pandas as pd
import json
import re

# Go To User Review URL and load all the reviews

date_list = []
username_list = []
# user_details_list = []

subscriber_list = []
user_review_list = []

rating_list = []
text_list = []
# useful_list = []

loop_count = 0
pagenumber = 1


#TODO Find the review number and divide by number of reviews on page, or find the number of pages
number_reviews = 22


# film_name = input("Enter the title of film: ")
# url_input = input("Enter URL of User Reviews: ")

url_input = 'http://www.allocine.fr/film/fichefilm-43921/critiques/spectateurs/'

for page in range(number_reviews):


    url = url_input + '?page=' + str(pagenumber)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')

    pagenumber += 1

    loop_count = 0


    for review in bs.findAll('div', {'class': 'hred review-card cf'}):
    
        # Rating
        rating = str(review.find("span", {"class": "stareval-note"}).contents)
        
        # Username
        username = review.findAll("span")[1].contents
        username = ''.join(username)

        # Gets Subscriber and User Review numbers
        try:
                user_details = str(review.find("p", {"class": "meta-content light"}).contents)
                user_details = re.sub("<span.*>", "", user_details)
                user_details = re.sub("</span>", "", user_details)
                user_details = re.sub("'\\n'", "", user_details)
                user_details = user_details.replace("'\\n'", "")
                user_details = user_details.replace(",", "")
                user_details = user_details.replace("[", "")
                user_details = user_details.replace("]", "")
                user_details = user_details.replace("Suivre son activité", "")
                user_details = user_details.strip()
                

                # Look for single review and get their subscriber number (if it exists)
                single_review = re.search(r'\bcritique\b', user_details)
                if single_review != None:
                        user_reviews = 1
                        stripped = re.findall(r"\b\d+\b", user_details)
                        if stripped:
                                subscribers = stripped[0]
                        else:
                                subscribers = 0

                # Gets the numbers from the user_details and separates them
                stripped = re.findall(r"\b\d+\b", user_details)


                # if there three digits the first is subscribers and latter two are followers
                if len(stripped) == 3:
                        subscribers = stripped[0]
                        user_reviews = stripped[1] + stripped[2]
                        # print(subscribers)
                        # print(user_reviews)
                # if there's two number separate them in to subscriber for first and followers second
                elif len(stripped) == 2:
                        subscribers = stripped[0]
                        user_reviews = stripped[1]
                        # print(subscribers)
                        # print(user_reviews)
                # If there's only one number we figure out if its a subscriber or number of reviews
                elif len(stripped) == 1:
                        if re.search(r'\bcritiques\b', user_details) != None:
                                subscribers = 0
                                user_reviews = stripped[0]
                        else:
                                subscribers = stripped[0]
                                user_reviews = 'Not Given'             


        except:
                user_details = 'No User Details'


        # Date
        # date = review.find("span", {"class": "review-card-meta-date light" })
        # date_text = date.text
        # date_text_strip = re.sub("[^0-9/]", "", date_text)

        # Review Text
        review_text = bs.findAll("div", attrs={"class": "content-txt review-card-content"})[loop_count]
        text = review_text.text
        loop_count += 1

        # Usefulness 
        usefulness = bs.findAll("div", {"class": "review-card-social"})
        # print(usefulness)

        #TODO Format username and ratings to not have square brackets or inverted commmas

        #TODO Add happy face, sad face


        # if the username is equal to the rating that means the user is a vistor and hasnt registered
        if username == rating:
                username = 'A Visitor'
                subscribers = 0
                user_reviews = 0

        # Add to list
        username_list.append(username)
        subscriber_list.append(subscribers)
        user_review_list.append(user_reviews)
        rating_list.append(rating)
        text_list.append(text)
    

# Create dataframe
review_data = pd.DataFrame(
    {
     'Username': username_list,
     'Subscribers': subscriber_list,
     'No. of Reviews': user_review_list,
     'Rating (out of 5)': rating_list,
     'Review Text': text_list,
     }
)


#JSOn data co to CSV
# csv_name = film_name
review_data.to_csv('CACHE.csv')

