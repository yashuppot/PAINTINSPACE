from pygame import *

width,height=800,600
screen=display.set_mode((width,height))
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)

canvasRect=Rect(100,80,500,300)
draw.rect(screen, GREEN, canvasRect,2)
screencap = screen.subsurface(canvasRect).copy()
running=True

while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type == MOUSEBUTTONDOWN:
            sx,sy = evt.pos
        if evt.type == MOUSEBUTTONUP:
            screen.blit(screencap,(100,80))
            draw.line(screen,GREEN, (sx,sy), (mx,my))
            screencap = screen.subsurface(canvasRect).copy()
            
                       
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    screen.set_clip(canvasRect)
    if mb[0] == 1:
        screen.blit(screencap,(100,80))
        draw.rect(screen, GREEN, canvasRect,2)
        draw.line(screen,GREEN, (sx,sy), (mx,my))
   
    display.flip()
            
quit()
