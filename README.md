# Apod-Twitter-Bot

NASA currently has an @APOD twitter account, which posts an Astronomy Picture of the Day each day. However, I noticed that there was no account posting past pictures of the day. As someone who has an interest in space, I wanted to see old APOD pictures in my twitter feed and was curious to see how twitter bots were built in general. Therefore, using NASA's API and Twitter's REST API, I created an twitter bot, @apod_archive, that tweets APOD images of that day from NASA's APOD archive, which contains over 20 years of images. For example, if today was Aug. 16, the bot will tweet the apod from a random past year for Aug. 16.

NOTE: The files in the repo are the code for the twitter bot. However, running main.py will not correctly run the program. This is because I have not added the twitter_creds.py which contains the Twitter API information.
