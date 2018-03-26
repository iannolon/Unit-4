#IanNolon
#3/26/18
#colorChangeWindow.py

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
    r = randint(1,17)
    if r == 1:
        screen = RectangleAsset(2000,1000,blackOutline,black)
        Sprite(screen)
    elif r == 2:
        screen = RectangleAsset(2000,1000,blackOutline,aqua)
        Sprite(screen)
    elif r == 3:
        screen = RectangleAsset(2000,1000,blackOutline,gray)
        Sprite(screen)
    elif r == 4:
        screen = RectangleAsset(2000,1000,blackOutline,navy)
        Sprite(screen)
    elif r == 5:
        screen = RectangleAsset(2000,1000,blackOutline,silver)
        Sprite(screen)
    elif r == 6:
        screen = RectangleAsset(2000,1000,blackOutline,green)
        Sprite(screen)
    elif r == 7:
        screen = RectangleAsset(2000,1000,blackOutline,olive)
        Sprite(screen)
    elif r == 8:
        screen = RectangleAsset(2000,1000,blackOutline,teal)
        Sprite(screen)
    elif r == 9:
        screen = RectangleAsset(2000,1000,blackOutline,blue)
        Sprite(screen)
    elif r == 10:
        screen = RectangleAsset(2000,1000,blackOutline,lime)
        Sprite(screen)
    elif r == 11:
        screen = RectangleAsset(2000,1000,blackOutline,purple)
        Sprite(screen)
    elif r == 12:
        screen = RectangleAsset(2000,1000,blackOutline,white)
        Sprite(screen)
    elif r == 13:
        screen = RectangleAsset(2000,1000,blackOutline,maroon)
        Sprite(screen)
    elif r == 14:
        screen = RectangleAsset(2000,1000,blackOutline,red)
        Sprite(screen)
    elif r == 15:
        screen = RectangleAsset(2000,1000,blackOutline,yellow)
        Sprite(screen)
    elif r == 16:
        screen = RectangleAsset(2000,1000,blackOutline,fuchsia)
        Sprite(screen)


App().listenMouseEvent('click',mouseClick)
App().run()
