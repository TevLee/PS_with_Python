# 브론즈 II
# https://www.acmicpc.net/problem/2798
# 10분(220217) : 조합
from itertools import permutations
from math import perm
n,m = map(int,input().split())
cards = list(map(int,input().split()))
perms = list(permutations(cards,3))
answer = 0
for perm in perms:
    tmp = sum(perm)
    if tmp <= m and tmp>answer:
        answer = tmp
print(answer) 
