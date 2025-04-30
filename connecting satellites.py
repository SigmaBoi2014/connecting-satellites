import random
import pgzrun
from time import time
WIDTH=600
HEIGHT=450
game_over=False

start = time()
sat=[]
next=0
lines=[]
total=0
for i in range(10):
    satellite=Actor("satellite")
    satellite.x = random.randint(30,560)
    satellite.y = random.randint(30,420)
    sat.append(satellite)
def draw():
    global total
    screen.blit("background",(0,0))
    num=1
    for i in sat:
        i.draw()
        screen.draw.text(str(num),(i.x,i.y+15),color = "red")
        num=num+1
    for line in lines:
        screen.draw.line(line[0],line[1],"red")
    if(next<10):
        
        total = time() - start
        screen.draw.text(str(round(total,2)),(10,10),color="yellow")
    else:
        screen.draw.text(str(round(total,2)),(10,10),color="yellow")
    if game_over:
        screen.fill("black")
        screen.draw.text("Time's up! You lost",midtop=(WIDTH/2,10),fontsize=40,color="red")
    if(next==10):
        screen.fill("black")
        screen.draw.text("Good Job! You Won!",midtop=(WIDTH/2,10),fontsize=40,color="green")
def update():
    pass
def time_up():
    global game_over,you_won
    game_over=True
def on_mouse_down(pos):
    global next,sat,lines
    if sat[next].collidepoint(pos):
        if next>0:
            lines.append((sat[next-1].pos,sat[next].pos))
            print(lines)
        next=next+1
    else:
        lines=[]
        next=0
clock.schedule(time_up,30.00)


pgzrun.go()