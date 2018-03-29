#IanNolon
#3/28/18
#warmup12.py - write a function that returns the GCF of two numbers

def GCF(a,b):
    for i in range(a+1,0,-1):
        if a%i == 0:
            if b%i == 0:
                return i
print(GCF(16,64))

