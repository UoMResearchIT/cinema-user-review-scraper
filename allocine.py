# Allo Cine User Review Scraper

# Currently does the first page (about 25 reviews, can loop over the URL later to get all the reviews, still need to exctract text and usefulness)

# Import libraries
from bs4 import BeautifulSoup 
import requests, sys, webbrowser, bs4
import pandas as pd
import json
import re

#Lists of all the different componenets of the data

# Username
username_list = []
# Number of subscribers the user has
subscriber_list = []
# Number of reviews the user has written
user_review_list = []
# User rating for the film 
rating_list = []
# Text of the review
text_list = []
# Date List
date_list = []

# Usefulness list (helpful/not helpful)
usefulreview_list = []
notusefulreview_list = []

# Member of 300 Club
sparta_list = []

# French Date
french_date_list = []

notes = []


# Don't change these variables. They keep count of the loops
loop_count = 0
pagenumber = 1

#TODO Find the review number and divide by number of reviews on page, or find the number of pages
film_name = input("Enter the title of film: ")
url_input = input("Enter URL of User Reviews: ")
number_reviews = int(input("Enter number of pages of reviews: "))


for page in range(number_reviews):

    # Page URL
    url = url_input + '?page=' + str(pagenumber)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')

    pagenumber += 1

    loop_count = 0
    
    # Usefulness # uses the whole soup so put the whole pages into a list, then when each review is looped over I add the first two objects
    # in the list then delete them, and so on

    usefulness_list = []

    for node in bs.findAll("a", {"class": "button button-xs button-helpful button-disabled"}):
                    usefulness = ''.join(node.findAll(text=True))
                    usefulness_list.append(usefulness)

    # Finds the reviews in the Beautiful Soup, and parses it for the different parts 
    for review in bs.findAll('div', {'class': 'hred review-card cf'}):

        # print(review)


        # Date
        date = review.find("span", {"class": "review-card-meta-date light" })
        # date = review.find("span", {"class": "review-card-meta-date light" })
        date_text = date.text
        date_text = date_text.replace("Publiée le", "")
        date_text = date_text.replace("\n", "")
        date_text = str(date_text)

        french_date = date_text
        
        try:
                date_text = date_text.replace("janvier", "/01/")
                date_text = date_text.replace("février", "/02/")
                date_text = date_text.replace("mars", "/03/")
                date_text = date_text.replace("avril", "/04/")
                date_text = date_text.replace("mai", "/05/")
                date_text = date_text.replace("juin", "/06/")
                date_text = date_text.replace("juillet", "/07/")
                date_text = date_text.replace("août", "/08/")
                date_text = date_text.replace("septembre", "/09/")
                date_text = date_text.replace("octobre", "/10/")
                date_text = date_text.replace("novembre", "/11/")
                date_text = date_text.replace("décembre", "/12/")
        except:
                date_text = 'No Date'
                
        date_text = date_text.replace(" ", "")

        

    
        # Rating
        rating = str(review.find("span", {"class": "stareval-note"}).contents)
        rating = rating[2:5]

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
                # if there's two number separate them in to subscriber for first and followers second
                elif len(stripped) == 2:
                        subscribers = stripped[0]
                        user_reviews = stripped[1]
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



        # Review Text
        review_text = bs.findAll("div", attrs={"class": "content-txt review-card-content"})[loop_count]
        text = review_text.text
        loop_count += 1

        # Usefulness
        useful_review = usefulness_list[0]
        not_useful_review = usefulness_list[1]
        del usefulness_list[:2]


        # if the username is equal to the rating that means the user is a vistor and hasnt registered
        if username == rating:
                username = 'A Visitor'
                subscribers = 0
                user_reviews = 0


                
        # Look for 300 Club                
        
        sparta = review.findAll("img", attrs={"title": "Membre du Club 300 Allociné"})
        
        if sparta :
                sparta = 'Yes'
        else:
                sparta = 'No'


        # Add to list
        username_list.append(username)
        date_list.append(date_text)
        subscriber_list.append(subscribers)
        user_review_list.append(user_reviews)
        rating_list.append(rating)
        text_list.append(text)
        usefulreview_list.append(useful_review)
        notusefulreview_list.append(not_useful_review)
        sparta_list.append(sparta)
        french_date_list.append(french_date)
    

# Create dataframe
review_data = pd.DataFrame(
    {
     'Username': username_list,
     'Subscribers': subscriber_list,
     'No. of Reviews': user_review_list,
     'Date of Review': date_list,
     'French Date': french_date_list,
     'Rating (out of 5)': rating_list,
     'Review Text': text_list,
     'Helpful': usefulreview_list,
     'Not Helpful': notusefulreview_list,
     '300 Club': sparta_list,
     }
)

review_data['Notes'] = ''

review_data['Date of Review'] =  pd.to_datetime(review_data['Date of Review'], format='%d/%m/%Y')

review_data['Date of Review'] = review_data['Date of Review'].dt.strftime('%d/%m/%Y')


#JSOn data co to CSV
csv_name = film_name
review_data.to_csv(csv_name + '_allocine.csv')

