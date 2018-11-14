from sense_hat import SenseHat
import requests

sense = SenseHat()

apikey = "3g25yMcEXasRcGshlTxbCTupYLcHSg9i"
city = "Roskilde"

location = requests.get('http://dataservice.accuweather.com/locations/v1/cities/search?apikey=' + apikey + '&q=' + city)
locationdata = location.json()
locationkey = locationdata[0]['Key']
locationname = locationdata[0]['LocalizedName']

weather = requests.get('http://dataservice.accuweather.com/locations/v1/cities/search?apikey=' + apikey + '&q=' + city)
weatherdata = weather.json()
temptext = weatherdata[0]['WeatherText']
temp = weatherdata[0]['Temperature']['Metric']['Value']

black = (0, 0, 0)
white = (155, 155, 155)

while True:
  sense.show_message("Temperatur i " + locationname + ": " + temp + "C" + " ... " + temptext, text_colour=white, back_colour=black, scroll_speed=0.05)

