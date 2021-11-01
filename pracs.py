'''import os

def sum(x, n):
    total = 1.0
    for i in range (2, n + 1):
        total = total + ((pow(x, i) - i) / (i))
    return total


if __name__== '__main__':
    x = int(os.getenv("x"))
    n = int(os.getenv("n"))
    print ("Sum is: {0:.4f}".format(sum(x, n)))'''

import os
n = int(os.getenv("n")) 
x = int(os.getenv("x")) 

sum1 = 1

for i in range(2,n+1):
    sum1 = sum1 + (((x**i)-i)/i)
print("The sum of series is ",round(sum1,2))
    

