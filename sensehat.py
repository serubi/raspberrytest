from sense_hat import SenseHat
import time
sense = SenseHat()
sense.clear()

def auto_rotate_display():
  # read sensors data to detect orientation
  x = round(sense.get_accelerometer_raw()['x'], 0)
  y = round(sense.get_accelerometer_raw()['y'], 0)

  rot = 0
  if x == -1:
    rot=90
  elif y == -1:
    rot=180
  elif x == 1:
    rot=270

  # rotate the display according to the orientation
  print ("Current orientation x=%s y=%s  rotating display by %s degrees" % (x, y, rot))
  sense.set_rotation(rot)

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)

for y in range(0, 8):
  for x in range(0, 4):
    if x % 2 == 0:
      sense.set_pixel(x, y, white)
    else:
      sense.set_pixel(x, y, red)

for y in range(0, 4):
  for x in range(4, 8):
    if x % 2 == 0:
      if y % 2 == 0:
        sense.set_pixel(x, y, white)
        sense.set_pixel(x, y, white)
        sense.set_pixel(x+1, y+1, white)
        sense.set_pixel(x+1, y+1, white)
      else:
        sense.set_pixel(x, y, blue)
        sense.set_pixel(x, y, blue)
        sense.set_pixel(x+1, y-1, blue)
        sense.set_pixel(x+1, y-1, blue)

for y in range(4, 8):
  for x in range(4, 8):
    if x % 2 == 0:
      sense.set_pixel(x, y, white)
    else:
      sense.set_pixel(x, y, red)

while True:
  auto_rotate_display()
