#IanNolon
#3/26/18
#warmup11.py - returns True if a number is prime and False otherwise

def prime(num):
    a=0 #a is just a variable to store True/False data outside of the for loop
    for i in range (2,num):
        if num % i == 0:
            a=1
    if a == 1 or num <= 1:
        return False
    else:
        return True
print(prime(3))
