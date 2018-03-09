#IanNolon
#3/9/18
#functionDemo.py - how to write our own functions

def hw():
    print("hello, world")
    
hw() #test of hello world function
hw() #another one
    
def double(thingToDouble):
    print(thingToDouble*2)

double(12) #test of double function
double('w') #test of double with a string input
double(False) #test of double with a boolean

def bigger(a,b):
    if a>b:
        print(a)
    elif b>a:
        print(b)
    else:
        print(a)
        
bigger(3,4)
bigger('Ian','Nolon') #later in the alphabet means bigger, not how many characters it has
bigger(True,False)

def slope(x1, y1, x2, y2):
    print((y2 - y1)/(x2 - x1))
    
slope(1,1,2,2)
slope(True,True,False,False)
