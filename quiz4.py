#IanNolon
#4/2/18
#quiz4.py

def count(num):
    for i in range (1,num+1):
        print(i)
def excitedPrint(sen):
    print(sen.upper(),'!!!')
def firstLetter(string):
    for ch in string:
        return (ch)
        break
def repeats(n1,n2,n3):
    if n1 == n2 or n1 == n3 or n2 == n3:
        return(True)
    else:
        return(False)

count(7)
excitedPrint('I <3 Programming')
print(firstLetter('Smedinghoff'))
print(repeats(5,6,5))
