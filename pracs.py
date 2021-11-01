import os

def sum(x, n):
    total = 1.0
    for i in range (2, n + 1):
        total = total + ((pow(x, i) - i) / (i))
    return total


if __name__== '__main__':
    x = int(os.getenv("x"))
    n = int(os.getenv("n"))
    print ("Sum is: ",sum(x, n))
    

