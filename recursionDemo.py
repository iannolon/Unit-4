#IanNolon
#3/28/18
#recursionDemo.py - recursve version of countdown

def countdownr(n):
    if n == 0: #base case
        print('BOOM!')
    else: #recursive step
        print(n)
        countdownr(n-1)
countdownr(5)
