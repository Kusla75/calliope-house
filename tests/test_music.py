from calliope_mini import *
import music

# list of pitch values. Every value 
# represents a frequency (Hz)
melody = [200, 300, 200, 300, 200, 
300, 100, 300, 100, 300, 100, 300, 
400, 300, 400, 300, 500, 600, 700, 300, 200]

pom = True
# image object can be created and then passed to
# the display and drawn. Every five numbers between :
# represent one row on the display
img_1 = Image('09090:90909:09090:90909:09090:')
img_2 = Image('90909:09090:90909:09090:90909:')

# this function plays a melody and switches between 
# two display patterns .This function can be improved 
# using multiprocessing
def play(pom, img_1, img_2):
    music.stop()
    for p in melody:
        music.pitch(p)
        if pom:
            display.show(img_1)
            pom = False
        else: 
            display.show(img_2)
            pom = True
        sleep(200)

while True:
    play(pom, img_1, img_2)
    