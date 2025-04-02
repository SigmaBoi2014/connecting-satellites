import random
import pgzrun

WIDTH=600
HEIGHT=450
satellite=Actor("satellite")
def draw():
    screen.blit("background",(0,0))
    satellite.draw()




pgzrun.go()