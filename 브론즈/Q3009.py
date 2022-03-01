a,aa = map(int,input().split())
b,bb = map(int,input().split())
c,cc = map(int,input().split())
if a==b:
    d = c
elif a==c:
    d = b
else :
    d = a
if aa==bb:
    dd = cc
elif aa==cc:
    dd = bb
else :
    dd = aa
print(d,dd)