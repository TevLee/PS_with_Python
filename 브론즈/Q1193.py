# 1 2 4 7 11 16
# 2 3 4 5 6 7
x = int(input())
s = 0
n = 1
while s<x:
    s+=n
    n+=1
cha = s-x
a,b = n-1,1
for i in range(cha):
    a-=1
    b+=1
if n%2==0:
    print(str(b)+"/"+str(a))
else :
    print(str(a)+"/"+str(b))

