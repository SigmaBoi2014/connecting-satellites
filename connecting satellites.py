import random
import pgzrun
WIDTH=600
HEIGHT=450
sat=[]
next=0
lines=[]
for i in range(10):
    satellite=Actor("satellite")
    satellite.x = random.randint(30,560)
    satellite.y = random.randint(30,420)
    sat.append(satellite)
def draw():
    screen.blit("background",(0,0))
    num=1
    for i in sat:
        i.draw()
        screen.draw.text(str(num),(i.x,i.y+15),color = "red")
        num=num+1
    for line in lines:
        screen.draw.line(line[0],line[1],"red")
def on_mouse_down(pos):
    global next,sat,lines
    if sat[next].collidepoint(pos):
        if next>0:
            lines.append((sat[next-1].pos,sat[next].pos))
            print(lines)
            next=next+1

pgzrun.go()