from sense_hat import SenseHat
import requests
import sys

sense = SenseHat()

apikey = "3g25yMcEXasRcGshlTxbCTupYLcHSg9i"

if len(sys.argv) > 1:
  city = sys.argv[1]
else:
  city = "Roskilde"
  
if len(sys.argv) > 2:
  city += " " + sys.argv[2]

print("Finder vejr for " + city)

location = requests.get('http://dataservice.accuweather.com/locations/v1/cities/search?apikey=' + apikey + '&q=' + city)
locationdata = location.json()

if len(locationdata) > 1:
  locationkey = locationdata[0]['Key']
  locationname = locationdata[0]['LocalizedName']

  weather = requests.get('http://dataservice.accuweather.com/currentconditions/v1/' + locationkey + '?apikey=' + apikey + '&q=' + city)
  weatherdata = weather.json()
  temptext = weatherdata[0]['WeatherText']
  temp = weatherdata[0]['Temperature']['Metric']['Value']

  black = (0, 0, 0)
  white = (255, 255, 255)

  while True:
    sense.show_message("Temperature in " + locationname + ": " + str(temp) + "C" + " ... " + temptext, text_colour=white, back_colour=black, scroll_speed=0.05)
else:
  red = (155, 0, 0)
  white = (255, 255, 255)

  while True:
    sense.show_message('The city "' + city + '" doesn\' exist!', text_colour=white, back_colour=red, scroll_speed=0.05)
