from sense_hat import SenseHat

sense = SenseHat()
orientation = sense.get_orientation_degrees()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

while True:
  sense.show_letter(str(**orientation))
  time.sleep(0.1)
