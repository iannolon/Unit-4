#IanNolon
#3/26/18
#bubbles.py

from ggame import *
from random import randint

black = Color(0x000000,1)
aqua = Color(0x00FFFF,1)
gray = Color(0x8B8680,1)
navy = Color(0x000080,1)
silver = Color(0xC0C0C0,1)
green = Color(0x01A368,1)
olive = Color(0x808000,1)
teal = Color(0x008080,1)
blue = Color(0x0066FF,1)
lime = Color(0x00FF00,1)
purple = Color(0x800080,1)
white = Color(0xFFFFFF,1)
maroon = Color(0x800000,1)
red = Color(0xED0A3F,1)
yellow = Color(0xFBE870,1)
fuchsia = Color(0xFF00FF,1) #original 16 end here
brown = Color(0xAF593E,1)
orange = Color(0xFF861F,1)
redOrange = Color(0xFF3F34,1)
skyBlue = Color(0x76D7EA,1)
violet = Color(0x8359A3,1)
yellowGreen = Color(0xC5E17A,1)
aquaGreen = Color(0x03BB85,1)
goldenYellow = Color(0xFFDF00,1)
jadeGreen = Color(0x0A6B0D,1)
lightBlue = Color(0x8FD8D8,1)
lightBrown = Color(0xA36F40,1)
magenta = Color(0xF653A6,1)
mahogany = Color(0xCA3435,1)
peach = Color(0xFFCBA4,1)
pink = Color(0xFF99CC,1)
tan = Color(0xFA9D5A,1) #32 colors
yellowOrange = Color(0xFFAE42,1)

blackOutline = LineStyle(1,black)

def printBubble(color):
    bubble = CircleAsset(randint(25,100),blackOutline,color)
    Sprite(bubble,(randint(-50,850),randint(-50,450)))

def mouseClick(event):
    r = randint(1,33) 
    if r == 1:
        printBubble(black)
    elif r == 2:
        printBubble(aqua)
    elif r == 3:
        printBubble(gray)
    elif r == 4:
        printBubble(navy)
    elif r == 5:
        printBubble(silver)
    elif r == 6:
        printBubble(green)
    elif r == 7:
        printBubble(olive)
    elif r == 8:
        printBubble(teal)
    elif r == 9:
        printBubble(blue)
    elif r == 10:
        printBubble(lime)
    elif r == 11:
        printBubble(purple)
    elif r == 12:
        printBubble(white)
    elif r == 13:
        printBubble(maroon)
    elif r == 14:
        printBubble(red)
    elif r == 15:
        printBubble(yellow)
    elif r == 16:
        printBubble(fuchsia)
    elif r == 17:
        printBubble(brown)
    elif r == 18:
        printBubble(orange)
    elif r == 19:
        printBubble(redOrange)
    elif r == 20:
        printBubble(skyBlue)
    elif r == 21:
        printBubble(violet)
    elif r == 22:
        printBubble(yellowGreen)
    elif r == 23:
        printBubble(aquaGreen)
    elif r == 24:
        printBubble(goldenYellow)
    elif r == 25:
        printBubble(jadeGreen)
    elif r == 26:
        printBubble(lightBlue)
    elif r == 27:
        printBubble(lightBrown)
    elif r == 28:
        printBubble(magenta)
    elif r == 29:
        printBubble(mahogany)
    elif r == 30:
        printBubble(peach)
    elif r == 31:
        printBubble(pink)
    elif r == 32:
        printBubble(tan)
    elif r == 33:
        printBubble(yellowOrange)


App().listenMouseEvent('click',mouseClick)
App().run()
