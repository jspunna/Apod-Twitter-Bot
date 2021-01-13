from datetime import date
from nasa import *
from twitter import *

if __name__ == '__main__':

    today = date.today()
    month = today.strftime("%m")
    day = today.strftime("%d")
    year = today.strftime("%Y")

    nasa = NASA(month, day, year)
    apod_details = nasa.getRandomYear()

    twtr = Twitter(apod_details)
    twtr.authenticate()


