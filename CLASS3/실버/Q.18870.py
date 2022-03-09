# 실버 2
# 좌표 압출
# 2초 512MB
'''
n개 좌표

'''
from collections import deque
import sys
n = int(input()) # 1~100만
tnums = list(map(int,sys.stdin.readline().split()))
nums = sorted(tnums)

dq = deque([(nums[0],0)])
dic = {}
dic[nums[0]] = 0


for i in range(1,len(nums)):# 하나씩 보면서
    if nums[i]!=nums[i-1] : # 앞수랑다르면 
        dic[ nums[i] ] = dq[-1][1]+1 # dict에도 추가
        dq.append( (nums[i],dq[-1][1]+1) ) # dq[-1]+1해서 dq에 넣고

for num in tnums: # 하나씩 보면서
    print(dic[num],end=" ")# dict에서 찾기

# import sys 
# N = int(sys.stdin.readline()) 
# arr = list(map(int,sys.stdin.readline().split())) 
# arr2 = [] 
# arr2 = list(sorted(set(arr))) # set처리하고 정렬
# dic = {arr2[i]:i for i in range (len(arr2))} # arr2를 딕셔너리에 넣어서
# for i in arr: # 하나씩 읽으면서 딕셔너리에서 받아오기
#     print(dic[i],end=' ') 

