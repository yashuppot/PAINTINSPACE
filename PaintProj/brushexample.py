
from pygame import *
from random import randint
from math import *

init()
size = width, height = 800, 600
screen = display.set_mode(size)
GREEN=(0,255,0)
RED=(255,0,0)
BLACK=(0,0,0)
    
def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

mouse.set_visible(False)
running = True
while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
   
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    screen.fill(BLACK)    
    dx = mx - 400
    dy = my - 300
    dist = distance(400, 300, mx, my)
    for d in range(10,int(dist),10):
        dotX = dx * d / dist + 400
        dotY = dy * d / dist + 300
        draw.circle(screen, GREEN, (int(dotX), int(dotY)) , 3)        
    
    draw.circle(screen, RED, (400, 300) , 10)
    draw.circle(screen, RED, (int(mx), int(my)) , 10)
    display.flip()
    
    
quit()
