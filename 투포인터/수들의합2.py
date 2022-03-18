# 실버 3
# 수들의합2
# 0.5초 128MB
'''
https://www.acmicpc.net/problem/2003
4 2
1 1 1 1

3
'''
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
numbers = list(map(int,input().split()))
ans = 0
s=e=0
while s<N:
    tmp = sum(numbers[s:e+1])
    if tmp>= M or e==N-1:
        s+=1
        if tmp==M:
            ans+=1
    else:
        e+=1

print(ans)
