from sense_hat import SenseHat
import time

sense = SenseHat()
orientation = sense.get_orientation_degrees()
#print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

while True:
  sense.show_message("{yaw}".format(**orientation))
  time.sleep(0.1)
