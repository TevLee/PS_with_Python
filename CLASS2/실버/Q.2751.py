# 실버 5
# 수 정렬하기 2
# 2초 256MB
'''
N개의 수, 오름차순 
'''
import sys
n = int(sys.stdin.readline())
nums = sorted([int(sys.stdin.readline()) for _ in range(n)])
for num in nums:
    print(num)
