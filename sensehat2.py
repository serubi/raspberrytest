from sense_hat import SenseHat
import requests

sense = SenseHat()


response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = response.json()

print(data)
