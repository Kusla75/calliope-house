# This script sends low and high voltage throught pin1 every 500 miliseconds.
# Any connected LEDs, that are connected to pin1, will flicker every half a second

from calliope_mini import *

v = 0
while True:
    pin1.write_digital(v)
    sleep(500)
    v = not v # This just changes 1 to 0 and vice versa