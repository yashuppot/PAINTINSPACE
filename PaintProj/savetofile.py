
from pygame import *

width,height=800,600
screen=display.set_mode((width,height))
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
screen.fill(BLUE)
canvasRect = Rect(100,50,650,450)


running=True

while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button==3:
                image.save(screen.subsurface(canvasRect), "mar12.png")
                       
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    draw.rect(screen,BLACK,canvasRect,2)
    if mb[0] == 1:
        draw.circle(screen,BLACK,(mx,my),2)



   
    display.flip()
            
quit()
