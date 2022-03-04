# 실버 3
# 동전 0
# 1초 256MB
'''
N종류 동전(무한)
합을 K로 , 동전 최소개
'''
N,K = map(int,input().split()) # N : 1~10 , K : 1~ 10억
ns = []
answer = 0
for _ in range(N):
    ns.append(int(input()))
for i in range(len(ns)-1,-1,-1):
    if K//ns[i] >= 1:
        answer += K//ns[i]
        K %= ns[i]
print(answer)