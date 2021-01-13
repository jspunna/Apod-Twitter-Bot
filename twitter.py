import tweepy
import requests
import os
from twitter_creds import *
from datetime import datetime


class Twitter:

    def __init__(self, apod):
        self.apod = apod

    # login and authentication for apod_archive twitter account
    def authenticate(self):
        consumer_key = API_KEY
        consumer_secret = API_SECRET
        access_token = ACCESS_TOKEN
        access_token_secret = ACCESS_SECRET

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        self.prepareTweet(api)

    # prepare/organize the apod details for the tweet
    def prepareTweet(self, api):
        apod_date = self.apod['date']
        date_obj = datetime.strptime(apod_date, "%Y-%m-%d")
        converted_date = datetime.strftime(date_obj, "%b %d %Y")
        formatted_date = "Date: " + converted_date[:3] + "." + converted_date[3:6] + "," + converted_date[6:]

        month = date_obj.strftime("%m")
        day = date_obj.strftime("%d")
        year = date_obj.strftime("%y")
        web_url = "https://apod.nasa.gov/apod/ap" + year + month + day + ".html"
        read = "Read more at: " + web_url

        title = "Title: " + self.apod['title']
        image_url = self.apod['url']

        self.tweet(api, formatted_date, title, read, image_url)

    # Tweet out the apod details on Twitter
    def tweet(self, api, date, title, read, image_url):
        file = 'temp.jpg'
        request = requests.get(image_url)
        if request.status_code == 200:
            with open(file, 'wb') as image:
                for chunk in request:
                    image.write(chunk)

            api.update_with_media(file, status=(date + "\n" + title + "\n" + read +
                                                "\n#apod #astronomy #space #nasa \n"))
            os.remove(file)
        else:
            print("Unable to post image")


