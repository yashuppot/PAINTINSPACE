
from pygame import *
from tkinter import *
from tkinter import filedialog
root = Tk()
root.withdraw()
width,height=800,600
screen=display.set_mode((width,height))
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
canvasRect = Rect(150,150,500,400)
openRect = Rect(40,50,40,40)
saveRect = Rect(100,50,40,40)
draw.rect(screen,YELLOW,canvasRect)
draw.rect(screen,GREEN,openRect)
draw.rect(screen,BLUE,saveRect)
running=True
go = False
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1:
                go = True
        if evt.type == MOUSEBUTTONUP:
            go = False
                       
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    if saveRect.collidepoint(mx,my) and go:
        go = False
        fname=filedialog.asksaveasfilename(defaultextension=".png")
        if len(fname) > 0:
            image.save(screen.subsurface(canvasRect),fname)
    if openRect.collidepoint(mx,my):
        fname=filedialog.askopenfilename()
        print(fname)
    

    
    
    display.flip()
            
quit()
