# This script temperature sensor. It reads temperature value
# from sensor and it displays it on the display

from calliope_mini import *

while True:
    t = str(temperature())
    display.scroll(t + 'C')