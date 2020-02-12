# This script tests the temperature sensor. It reads temperature value
# from the sensor and it displays it on the LED display

from calliope_mini import *

while True:
    t = str(temperature())
    display.scroll(t + 'C')