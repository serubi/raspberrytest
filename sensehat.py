from sense_hat import SenseHat
import time
sense = SenseHat()
sense.clear()

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

while true:
  time.sleep(1)
  sense.flip_v()
  time.sleep(1)
  sense.flip_h()
