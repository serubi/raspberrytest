from sense_hat import SenseHat
import time
import math

sense = SenseHat()
#orientation = sense.get_orientation_degrees()
#print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

while True:
  orientation = sense.get_orientation_degrees()
  print("p: " + str(math.floor(orientation['pitch'])) + ", r: " + str(math.floor(orientation['roll'])) + ", y: " + str(math.floor(orientation['yaw'])))
  #sense.show_message(str(math.floor(orientation['yaw'])))
  #time.sleep(0.5)
