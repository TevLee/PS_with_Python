#고정비용 A, 생산비 B, 판매가 C
# C*n > A+B*n
a,b,c = map(int,input().split())
# (c-b)*n > A 인 n
# n > A/(c-b)
div = c-b
if c-b <=0:
    print(-1)
else :
    print(a//div+1)