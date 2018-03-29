#IanNolon
#3/26/18
#bubbles.py

from ggame import *
from random import randint

black = Color(0x000000,1)
aqua = Color(0x00FFFF,1)
gray = Color(0x808080,1)
navy = Color(0x000080,1)
silver = Color(0xC0C0C0,1)
green = Color(0x008000,1)
olive = Color(0x808000,1)
teal = Color(0x008080,1)
blue = Color(0x0000FF,1)
lime = Color(0x00FF00,1)
purple = Color(0x800080,1)
white = Color(0xFFFFFF,1)
maroon = Color(0x800000,1)
red = Color(0xFF0000,1)
yellow = Color(0xFFFF00,1)
fuchsia = Color(0xFF00FF,1)

blackOutline = LineStyle(1,black)

def mouseClick(event):
    r = randint(1,16) 
    if r == 1:
        bubble = CircleAsset(randint(10,150),blackOutline,fuchsia)
        Sprite(bubble,(randint(0,800),randint(0,400)))
    elif r == 2:
        bubble = CircleAsset(randint(10,150),blackOutline,aqua)
        Sprite(bubble,(randint(0,800),randint(0,400)))
    elif r == 3:
        bubble = CircleAsset(randint(10,150),blackOutline,gray)
        Sprite(bubble,(randint(0,800),randint(0,400)))
    elif r == 4:
        bubble = CircleAsset(randint(10,150),blackOutline,navy)
        Sprite(bubble,(randint(0,800),randint(0,400)))
    elif r == 5:
        bubble = CircleAsset(randint(10,150),blackOutline,silver)
        Sprite(bubble,(randint(0,800),randint(0,400)))
    elif r == 6:
        bubble = CircleAsset(randint(10,150),blackOutline,green)
        Sprite(bubble,(randint(0,800),randint(0,400)))
    elif r == 7:
        bubble = CircleAsset(randint(10,150),blackOutline,olive)
        Sprite(bubble,(randint(0,800),randint(0,400)))
    elif r == 8:
        bubble = CircleAsset(randint(10,150),blackOutline,teal)
        Sprite(bubble,(randint(0,800),randint(0,400)))
    elif r == 9:
        bubble = CircleAsset(randint(10,150),blackOutline,blue)
        Sprite(bubble,(randint(0,800),randint(0,400)))
    elif r == 10:
        bubble = CircleAsset(randint(10,150),blackOutline,lime)
        Sprite(bubble,(randint(0,800),randint(0,400)))
    elif r == 11:
        bubble = CircleAsset(randint(10,150),blackOutline,purple)
        Sprite(bubble,(randint(0,800),randint(0,400)))
    elif r == 12:
        bubble = CircleAsset(randint(10,150),blackOutline,white)
        Sprite(bubble,(randint(0,800),randint(0,400)))
    elif r == 13:
        bubble = CircleAsset(randint(10,150),blackOutline,maroon)
        Sprite(bubble,(randint(0,800),randint(0,400)))
    elif r == 14:
        bubble = CircleAsset(randint(10,150),blackOutline,red)
        Sprite(bubble,(randint(0,800),randint(0,400)))
    elif r == 15:
        bubble = CircleAsset(randint(10,150),blackOutline,yellow)
        Sprite(bubble,(randint(0,800),randint(0,400)))
    elif r == 16:
        bubble = CircleAsset(randint(10,150),blackOutline,black)
        Sprite(bubble,(randint(0,800),randint(0,400)))


App().listenMouseEvent('click',mouseClick)
App().run()
