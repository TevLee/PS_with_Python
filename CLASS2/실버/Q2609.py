# 실버 5
# 최대공약수와 최소공배수
# 1초 128MB
'''
최대 공약수, 최소공배수 출력
'''

def gcd(A,B):
    while B>0:
        tmp = A%B
        A = B
        B = tmp
    return A

A,B = map(int,input().split())
C = gcd(A,B)# 최대공약수(gcd) 구하고
print(C)
print((int)(A*B/C))# 최소공배수 = A*B / gcd
