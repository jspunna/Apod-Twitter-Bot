import random
import requests


class NASA:

    def __init__(self, m, d, y):
        self.month = m
        self.day = d
        self.year = y

    # get random year for the current month and day
    def getRandomYear(self):
        random_year = random.randint(1995, int(self.year) - 1)
        request_date = "" + str(random_year) + "-" + str(self.month) + "-" + str(self.day) + ""
        return self.getAPOD(request_date)

    # use year from getRandomYear() to get apod for this day in history of the archives
    def getAPOD(self, request_date):
        while True:
            request_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
            parameters = {
                'date': request_date
            }
            request = requests.get(request_url, params=parameters)
            print(request.status_code)
            if request.status_code == 200:
                return request.json()
            else:
                print("Something went wrong while retrieving the astronomy picture of the day from the archives")