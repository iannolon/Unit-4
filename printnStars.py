#IanNolon
#3/9/18
#printnStars.py

def printnStars(num):
    row = 0
    while row <num+1:
        print(' '*(num-row+1),' *'*row)
        row += 1

printnStars(21)
