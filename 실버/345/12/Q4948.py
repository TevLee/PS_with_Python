import math

def isPrime(num):
    if num<=1:
        return False
    else :
        limit = int(math.sqrt(num))
        for i in range(2,limit+1):
            if num%i==0:
                return False
        return True

while True:
    n = int(input())
    if n==0:
        break
    else:
        cnt = 0
        for i in range(n+1,2*n+1):
            if isPrime(i):
                cnt+=1
        print(cnt)