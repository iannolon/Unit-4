#IanNolon
#3/28/18
#triangle.py

def distance(X1,Y1,X2,Y2):
    return ((X2-X1)**2+(Y2-Y1)**2)**(1/2)
x1=int(input('x1 = '))
y1=int(input('y1 = '))
x2=int(input('x2 = '))
y2=int(input('y2 = '))
x3=int(input('x3 = '))
y3=int(input('y3 = '))
a = distance(x1,y1,x2,y2)
b = distance(x2,y2,x3,y3)
c = distance(x3,y3,x1,y1)
s = 1/2*(a+b+c)
print('Area = ',(s*(s-a)*(s-b)*(s-c))**(1/2))
