# 난이도 2
# (5분)/30분 1초 128MB
'''
오름차순 정렬된 수열 N개 원소 
x가 몇번 등장? (단,O(logN))
없으면 -1
'''
from bisect import bisect_left,bisect_right
N,x = map(int,input().split())
nums = list(map(int,input().split()))

def check():
    return bisect_right(nums,x)-bisect_left(nums,x)

print( check() if check()>0 else -1)
