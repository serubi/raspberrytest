from sense_hat import SenseHat
import requests

sense = SenseHat()


response = requests.get('https://reqres.in/api/users/2')
data = response.json()

print(data["first_name"])

black = (0, 0, 0)
blue = (0, 0, 255)

while True:
  sense.show_message(data["first_name"] + " " + data["last_name"], text_colour=blue, back_colour=black, scroll_speed=0.05)

