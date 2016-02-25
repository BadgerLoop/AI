import riffle
import forecastio
import json
import urllib2
import random
import os
from config import *
from riffle import want

class Recv(riffle.Domain):

    def onJoin(self):

        print 'Backend setup successfully'

        def message(s):
            print 'Received: ' + s #Messages received from frontend
            msgReturn = parser(s.lower())
            return msgReturn

        self.register("message", message)

def parser(s):
    if "weather" in s: 
        return weather()
    if any(hi in s for hi in hellomsgs): #Checks if any of the hellomsgs keywords are in the message
        return 'Hi there! How are you?'
    if any(musk in s for musk in muskmsg): #Checks if any of the hellomsgs keywords are in the message
        return random.choice(muskfacts)
    return "Sorry, I didn't understand what you said."
    
def weather(): 
    #Fetch lon and lat based on user IP
    data = json.load(urllib2.urlopen(location_fetcher))
    forecast = forecastio.load_forecast(forecast_api_key, data['lat'], data['lon'])
    return forecast.daily().summary

if __name__ == '__main__':
    riffle.SetFabric(os.environ['WS_URL'])
    domain = os.environ['DOMAIN']
    Recv(domain).join()
    exit()