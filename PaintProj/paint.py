from pygame import *
from random import *
from tkinter import *
from math import *
from tkinter import filedialog
font.init()
root = Tk()
root.withdraw()
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE = (255,255,255)
width,height = 1260, 820
###Image loading
background = image.load("img/backdrop.jpg") 
panel = image.load("img/pinkgrid.jpg")
panel = transform.scale(panel,(230,460))
background = transform.scale(background, (width, height))
pencilbutton = image.load("img/pencil.png")
rulerbutton = image.load("img/ruler.png")
eraserbutton = image.load("img/eraser.png")
brushbutton = image.load("img/brush.png")
colourpicker = image.load("img/colours.png")
filledrectanglebutton = image.load("img/filledrectangle.png")
unfilledrectanglebutton = image.load("img/unfilledrectangle.png")
filledellipsebutton = image.load("img/ellipse.png")
unfilledellipsebutton = image.load("img/hollowellipse.png")
spraypaintbutton = image.load("img/spray.png")
eyedropperbutton = image.load("img/eye-dropper.png")
dimx, dimy = 128,128
planet = image.load("img/planet.png")
planetbutton = transform.scale(planet, (dimx,dimy))
satellite = image.load("img/satellite.png")
satellitebutton = transform.scale(satellite, (dimx,dimy))
saturn = image.load("img/saturn.png")
saturnbutton = transform.scale(saturn, (dimx,dimy))
ship = image.load("img/start-up.png")
shipbutton = transform.scale(ship,(dimx,dimy))
stars = image.load("img/ursa-major.png")
starsbutton = transform.scale(stars, (dimx,dimy))
astronaut = image.load("img/astronaut.png")
astronautbutton = transform.scale(astronaut, (dimx,dimy))
savebutton = image.load("img/download.png")
uploadbutton =image.load("img/upload.png")
backx, backy = 140, 70
bg1 = image.load("img/ISS.jpg")
bg1button = transform.scale(bg1, (backx,backy))
bg2 = image.load("img/spacerock.jpg")
bg2button = transform.scale(bg2,(backx,backy))
bg3 = image.load("img/blackhole.jpg")
bg3button = transform.scale(bg3, (backx,backy))
###

###Canvas and screen creation
screen=display.set_mode((width,height))
screen.blit(background,(0,0))
titleFont = font.SysFont("Algerian", 75)
smallFont = font.SysFont("Times New Roman", 12)
titlePic = titleFont.render("PAINT IN SPACE", False, WHITE)
screen.blit(titlePic, (350,10))
screen.blit(panel,(30,190))
canvasRect = Rect(300,190,800,500) #Canvas on which the user can draw.
draw.rect(screen,WHITE,canvasRect)
draw.rect(screen,BLACK,canvasRect,3)
screencap = screen.subsurface(canvasRect).copy()
colourcanvasRect = Rect(canvasRect.right + 10,canvasRect.top + 3*backy + 220, backx, backy) #Rect which changes canvas colour when clicked
draw.rect(screen,WHITE,colourcanvasRect)
colourRect = Rect(15,715,222,106)
currentcolourRect = (247,821,50,-50) #Displays the selected colour
screen.blit(colourpicker, (colourRect.left, colourRect.top)) #Colour picker which can be clicked to select any colour on it.
topRect = Rect(canvasRect.left, canvasRect.top - 30, canvasRect.width, 30) #Top bar of canvas.
draw.rect(screen,WHITE,topRect)
draw.rect(screen,BLACK,topRect,5)
###




###Classes
class Button: #Button class with useful functions.
    def __init__(self,shape,tool,pic,outline):
        self.shape = shape
        self.rect = Rect(shape)
        self.pressed = False
        self.tool = tool
        self.pic = pic
        self.outline = outline

    def drawbut(self):
        'Draws button to screen'
        if self.outline: #Some buttons should not have an outline.
            draw.rect(screen,(0,0,100),self.rect,2)
        screen.blit(self.pic,(self.rect.left,self.rect.top))
                        
    
    def checkpressed(self):
        'Checks if the buton has been pressed'
        if self.rect.collidepoint((mx,my)) and pressstate == 1:
            self.pressed = True
        else:
            self.pressed = False
            
    def checkover(self):
        'Checks if user is hovering over button and highlights in dark green.'
        if self.rect.collidepoint(mx,my):
            draw.rect(screen,(0,100,0),(self.shape[0] - 2, self.shape[1]-2, self.shape[2]+4,self.shape[3]+4),2) #Outlines around the button.
            return True
        return False        
###           
        
###Buttons and tools 
buttons = [] #List of buttons that we will loop through.
button1 = Button((85,517,32,32),1,pencilbutton,True)
button2 = Button((85,417,32,32),2,eraserbutton,True)
button3 = Button((85,321,32,32),3,rulerbutton,True)
button4 = Button((85,221,32,32),4,brushbutton,True)
button5 = Button((159,221,32,32),5,filledrectanglebutton,True)
button6 = Button((159,321,32,32),6,unfilledrectanglebutton,True)
button7 = Button((159,417,32,32),7,filledellipsebutton,True)
button8 = Button((159,517,32,32),8,unfilledellipsebutton,True)
button9 = Button((159,615,32,32),9,spraypaintbutton,True)
button10 = Button((85,615,32,32),10,eyedropperbutton,True)
button11 = Button((300,700,dimx,dimy),11,planetbutton,False)
button12 = Button((430,700,dimx,dimy),12,satellitebutton,False)
button13 = Button((560,700,dimx,dimy),13,saturnbutton,False)
button14 = Button((690,700,dimx,dimy),14,shipbutton,False)
button15 = Button((820,700,dimx,dimy),15,starsbutton,False)
button16 = Button((960,700,dimx,dimy),16,astronautbutton,False)
button17 = Button((topRect.right - 20,topRect.top+5,16,16),17,savebutton,False)
button18 = Button((topRect.right - 40,topRect.top+5,16,16),18,uploadbutton,False)
button19 = Button((canvasRect.right + 10,canvasRect.top,backx,backy),19,bg1button,False)
button20 = Button((canvasRect.right + 10,canvasRect.top + backy + 60,backx,backy),20,bg2button,False)
button21 = Button((canvasRect.right + 10,canvasRect.top + 2*backy + 140,backx,backy),21,bg3button,False)
buttons.append(button1)
buttons.append(button2)
buttons.append(button3)
buttons.append(button4)
buttons.append(button5)
buttons.append(button6)
buttons.append(button7)
buttons.append(button8)
buttons.append(button9)
buttons.append(button10)
buttons.append(button11)
buttons.append(button12)
buttons.append(button13)
buttons.append(button14)
buttons.append(button15)
buttons.append(button16)
buttons.append(button17)
buttons.append(button18)
buttons.append(button19)
buttons.append(button20)
buttons.append(button21)
###

tools = ["none", "penicl", "erase", "line","brush","filledrectangle","unfilledrectangle","filledellipse","unfilledellipse","spraypaint","eyedropper","planet","satellite","saturn","ship","stars","astronaut","save","upload","bg1","bg2","bg3"] #List of tools.
tool = 0
size = 40 #Default tool size
col = WHITE #Default tool colour
bgcol = WHITE #Default background colour
for i in buttons:
    i.drawbut()
backcap = screen.subsurface((0,0,width,height)).copy() #Captures the whole screen after buttons drawn.

###



###Functions
def distance(x1,y1,x2,y2):
    'Returns distance between (x1,y1) and (x2,y2).'
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def buttonactions():
    'Draw to canvas based on the tool selected.'
    global tool
    global col
    global bgcol
    if canvasRect.collidepoint((mx,my)):
        screen.set_clip(canvasRect)
        if tools[tool] == "penicl" and mb[0] == 1:
            dx = mx - oldx
            dy = my - oldy
            dist = distance(oldx, oldy, mx, my)
            for d in range(0,int(dist),1):
                dotX = dx * d / dist + oldx 
                dotY = dy * d / dist + oldy
                draw.circle(screen, col, (int(dotX), int(dotY)) , min(size,5)) #Draws circles with radius at most 5 when mouse is pressed.

        elif tools[tool] == "erase" and mb[0] == 1:
            draw.circle(screen, bgcol, (mx,my), 4*size) #Draws circles that are the background colour (if background is an image we will defualt to white).

        elif tools[tool] == "line" and mb[0] == 1:
            screen.blit(curframe, (canvasRect.left,canvasRect.top)) #Draws current frame on every call to prevent multiple lines.
            draw.line(screen, col, (downx,downy), (mx,my)) #Draws a line from point where clicked to current position.
        elif tools[tool] == "brush" and mb[0] == 1:
            dx = mx - oldx
            dy = my - oldy
            dist = distance(oldx, oldy, mx, my)
            for d in range(0,int(dist),1):
                dotX = dx * d / dist + oldx 
                dotY = dy * d / dist + oldy
                draw.circle(screen, col, (int(dotX), int(dotY)) , 3*size) #Using similair triangles to draw as many circles as possible between the mouse position on the previous frame and the new position.
        elif tools[tool] == "filledrectangle" and mb[0] == 1:
            screen.blit(curframe, (canvasRect.left,canvasRect.top)) 
            draw.rect(screen,col,(downx,downy,mx-downx,my-downy)) #Draws a rectangle scaling out from the point where clicked.
        elif tools[tool] == "unfilledrectangle" and mb[0] == 1 and canvasRect.collidepoint((downx,downy)):
            screen.blit(curframe, (canvasRect.left,canvasRect.top))
            rectRect = Rect(downx,downy,mx-downx,my-downy)
            rectRect.normalize()
            draw.rect(screen,col,rectRect,2*size)
            for i in range(1,2*size):
                draw.rect(screen,col,(rectRect[0]-i,rectRect[1]-i,rectRect[2]+2*i,rectRect[3] + 2*i),1) #Drawing multiple rectangles, each bordering the previous, to fill in empty corner pixels.
        elif tools[tool] == "filledellipse" and mb[0] == 1:
            screen.blit(curframe, (canvasRect.left,canvasRect.top))
            try:
                ellRect = Rect(downx,downy,(mx-downx),(my-downy))
                ellRect.normalize() #draw.ellipse() only takes normalized Rects, no negatives.
                draw.ellipse(screen,col,ellRect)
            except:
                pass
        elif tools[tool] == "unfilledellipse" and mb[0] == 1:
            screen.blit(curframe, (canvasRect.left,canvasRect.top))
            try:
                ellRect = Rect(downx,downy,mx-downx,my-downy)
                ellRect.normalize()
                middleRect = (ellRect[0]+size,ellRect[1]+size,ellRect[2]-2*size,ellRect[3]-2*size) #Draws a ellipse with backgroound colour in centre to give an unfilled effect
                draw.ellipse(screen, col, ellRect)
                draw.ellipse(screen, bgcol, middleRect) #Draws a ellipse with backgroound colour in centre to give an unfilled effect
            except:
                pass
        elif tools[tool] == "spraypaint" and mb[0] == 1:
            points = [[mx + randint(-3*size,3*size), my + randint(-3*size,3*size)] for i in range(2*size)] #Random list of points to spray on.
            for x,y in points:
                if ((mx-x)**2 + (my-y)**2)**0.5 <= 3*size: #Only spray them if they are within a radius of 3*size from the mouse.
                    draw.circle(screen,col, (x,y), 1)
        if tools[tool] == "eyedropper" and canvasRect.collidepoint((downx,downy)):
            col = screen.get_at((downx,downy)) #Changes col to clicked pixel colour.
        ###Stamps
        elif tools[tool] == "planet" and mb[0] == 1 and canvasRect.collidepoint((downx,downy)):
            screen.blit(curframe,(canvasRect.left,canvasRect.top)) #Redraws curframe to stop trailing.
            screen.blit(planet,(mx-64,my-64)) #Draws stamp centred at the mouse.
        elif tools[tool] == "satellite" and mb[0] == 1 and canvasRect.collidepoint((downx,downy)):
            screen.blit(curframe,(canvasRect.left,canvasRect.top))
            screen.blit(satellite,(mx-64,my-64))
        elif tools[tool] == "saturn" and mb[0] == 1 and canvasRect.collidepoint((downx,downy)):
            screen.blit(curframe,(canvasRect.left,canvasRect.top))
            screen.blit(saturn,(mx-64,my-64))
        elif tools[tool] == "ship" and mb[0] == 1 and canvasRect.collidepoint((downx,downy)):
            screen.blit(curframe,(canvasRect.left,canvasRect.top))
            screen.blit(ship,(mx-64,my-64))
        elif tools[tool] == "stars" and mb[0] == 1 and canvasRect.collidepoint((downx,downy)):
            screen.blit(curframe,(canvasRect.left,canvasRect.top))
            screen.blit(stars,(mx-64,my-64))
        elif tools[tool] == "astronaut" and mb[0] == 1 and canvasRect.collidepoint((downx,downy)):
            screen.blit(curframe,(canvasRect.left,canvasRect.top))
            screen.blit(astronaut,(mx-64,my-64))
        ###
        elif tools[tool] == "save":
            tool = 0
            fname=filedialog.asksaveasfilename(defaultextension=".png")
            if len(fname) > 0: #If the user cancels we can't save the canvas, since fname doesn't exist.
                image.save(screen.subsurface(canvasRect),fname)
        elif tools[tool] == "upload":
            tool = 0
            fname=filedialog.askopenfilename()
            if len(fname) > 0:
                try: #Incase the file the user tries to load is not an image we throw an exception.
                    pic = image.load(fname)
                    pic = transform.scale(pic, (canvasRect.width,canvasRect.height))
                    screen.blit(pic, (canvasRect.left, canvasRect.top))
                except:
                    pass
    ###Backgrounds
    elif tools[tool] == "bg1":
        bgcol = WHITE
        tool = 0
        newcanvas = transform.scale(bg1,(canvasRect.width-2, canvasRect.height-2)) #Fits background to canvas.
        screen.blit(newcanvas,(canvasRect.left+1,canvasRect.top+1)) #Draws background over canvas.
    elif tools[tool] == "bg2":
        bgcol = WHITE
        tool = 0
        newcanvas = transform.scale(bg2,(canvasRect.width-2, canvasRect.height-2))
        screen.blit(newcanvas,(canvasRect.left,canvasRect.top))
    elif tools[tool] == "bg3":
        bgcol = WHITE
        tool = 0
        newcanvas = transform.scale(bg3,(canvasRect.width-2, canvasRect.height-2))
        screen.blit(newcanvas,(canvasRect.left,canvasRect.top))
    screen.set_clip((0,0,width,height))
    ###

            
            
            

def selected():
    'Highlights the selected tool in light green.'
    for i in buttons:
        if tool == i.tool:
            draw.rect(screen,GREEN,(i.shape[0] - 2, i.shape[1]-2, i.shape[2]+4,i.shape[3]+4),2)

def drawbuttons():
    'Draws buttons and other objects that are not on the canvas.'
    found = False
    for i in buttons:
        i.drawbut()
        if i.checkover():
            screen.blit(backcap, (0,0)) #If we find a new button being hovered, we blit backcap which clears any other highlights, and then redraw the screencap to keep the canvas.
            screen.blit(screencap, (canvasRect.left,canvasRect.top))
            i.checkover() #We run checkover() again to draw the highlight.
            found = True
    if not found:
        screen.blit(backcap, (0,0)) #If nothing is hovered we blit backcap to clear highlights.
        screen.blit(screencap, (canvasRect.left,canvasRect.top))
    draw.rect(screen, col, currentcolourRect) #Redraws the colour preview box incase backcap was blitted over it.
    draw.rect(screen,col,colourcanvasRect) #Redraws the colour canvas box incase backcap was blitted over it.
    draw.rect(screen, BLACK, currentcolourRect,3) #Redraws the colour preview box highlight incase backcap was blitted over it.
###

    
###Main loop
running=True

while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1:
                downx, downy = mx, my #Coordinates at the clicked frame.
                pressstate = evt.button
                for i in buttons: #This loop checks if each button was pressed, and changes the tool and highlight accordingly.
                    i.checkpressed()
                    if i.pressed:
                        if tool == i.tool:
                            tool = 0
                        else:
                            tool = i.tool
                            size = 5
                if colourRect.collidepoint((downx,downy)):
                    col = screen.get_at((downx,downy)) #Changes col to clicked pixel colour.
                    draw.rect(screen,col,colourcanvasRect)
                curframe = screen.subsurface(canvasRect).copy() #Keeps a copy of the frame when we clicked so that we can blit it to avoid stamp trailing and multiples lines.
            if evt.button == 4:
                if size < 50: #User can increase drawing size as long as it is below 50
                    size += 1
            if evt.button == 5:
                if size > 0: #User can decrease drawing size as long as it is above 1.
                    size -= 1
        if evt.type == MOUSEBUTTONUP:
            screencap = screen.subsurface(canvasRect).copy() #Each time the mouse button is released we capture the screen and blit it.
            screen.blit(screencap, (canvasRect.left,canvasRect.top))
    draw.rect(screen,col,colourcanvasRect)       
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    drawbuttons()
    buttonactions()
    selected()
    if colourcanvasRect.collidepoint((mx,my)) and mb[0] ==1:
        bgcol = col #If the user clicks the colourcanvasRect, we change bgcol to col for the eraser.
        draw.rect(screen,bgcol,canvasRect) #We fill the canvas with selected colour.
    if canvasRect.collidepoint(mx,my):
        canx, cany = mx-canvasRect.left, my-canvasRect.top #Gets coordinates of mouse with respect to canvas.
        coordinates = smallFont.render(str(canx) + "," + str(cany), False, BLACK)
        screen.blit(coordinates, (topRect.left+5,topRect.top+5))
    
    display.flip()
    screencap = screen.subsurface(canvasRect).copy() #After every update we capture the screen.
    oldx, oldy = mx, my
quit()
