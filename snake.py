from sense_hat import SenseHat

sense = SenseHat()

# examples using (x, y, r, g, b)
sense.set_pixel(0, 0, 255, 0, 0)
sense.set_pixel(0, 7, 0, 255, 0)
sense.set_pixel(7, 0, 0, 0, 255)
sense.set_pixel(7, 7, 255, 0, 255)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# examples using (x, y, pixel)
sense.set_pixel(0, 0, red)
sense.set_pixel(0, 0, green)
sense.set_pixel(0, 0, blue)
