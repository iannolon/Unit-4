#IanNolon
#3/22/18
#monkeyBanana.py - the best game ever!!!

from ggame import *
from random import randint

#constants
ROWS = 20
COLS = 40
CELL_SIZE = 20
BANANA_SPEED = 180

#move monkey right one cell if possible
def moveRight(event):
    if monkey.x < (COLS-1)*CELL_SIZE:
        monkey.x += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
    
#move monkey left one cell if possible
def moveLeft(event):
    if monkey.x > 0:
        monkey.x -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
    
#move monkey up one cell if possible
def moveUp(event):
    if monkey.y > 0:
        monkey.y -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
    
#move monkey down one cell if possible
def moveDown(event):
    if monkey.y < (ROWS-1)*CELL_SIZE:
        monkey.y += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
    
#move banana to a random location and reset timer
def moveBanana():
    data['frames'] = 0 
    banana.x = randint(0,COLS-1)*CELL_SIZE
    banana.y = randint(0,ROWS-1)*CELL_SIZE
    
#increase score and display new text at bottom of screen
def updateScore():
    data['score'] += 10
    data['ScoreText'].destroy() #remove old writing
    scoreBox = TextAsset('Score = '+str(data['score']))
    data['ScoreText'] = Sprite(scoreBox,(0,ROWS*CELL_SIZE+10))

#keeps track of how many frames have happened and moves banana if it has been
#more than 300 frames since last move
def step():
    data['frames'] +=1
    if data['frames'] == BANANA_SPEED:
        moveBanana()

#sets up and runs the game
if __name__ == '__main__':
    
    #hold variables in a dictionary
    data = {}
    data['score'] = 0
    data['frames'] = 0
    
    #colors
    lakeColor = Color(0x0000FF,1)
    monkeyColor = Color(0x08E7AA,1)
    bananaColor = Color(0x52470B,1)
    
    #graphics
    lakeBox = RectangleAsset(CELL_SIZE*COLS,CELL_SIZE*ROWS,LineStyle(1,lakeColor),lakeColor)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,monkeyColor),monkeyColor)
    bananaBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,bananaColor),bananaColor)
    scoreBox = TextAsset('Score = 0')
    
    Sprite(lakeBox)
    monkey = Sprite(monkeyBox)
    banana = Sprite(bananaBox,(CELL_SIZE*COLS/2,CELL_SIZE*ROWS/2))
    data['ScoreText'] = Sprite(scoreBox,(0,ROWS*CELL_SIZE+10))
    
    App().listenKeyEvent('keydown','right arrow',moveRight)
    App().listenKeyEvent('keydown','left arrow',moveLeft)
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().listenKeyEvent('keydown','down arrow',moveDown)
    App().run(step)
