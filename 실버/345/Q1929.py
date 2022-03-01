import sys,math
def isPrime(num):
    if num<=1:
        return False
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                return False
        return True

m,n = map(int,sys.stdin.readline().split())
for i in range(m,n+1):
    if isPrime(i):
        print(i)