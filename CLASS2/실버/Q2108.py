# 실버 3
# 통계학
# 2초 256MB
'''
N개수 
'''
from collections import Counter
import sys

N = int(sys.stdin.readline()) # 1~50만
nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort()
# 산술평균
print(round(sum(nums)/len(nums)))
# 중앙값
print(nums[len(nums)//2])
# 최빈값
cnt = Counter(nums).most_common(2)
# print(cnt, type(cnt))
if len(nums)>1:
    print(cnt[1][0] if cnt[0][1]==cnt[1][1] else cnt[0][0])
else :
    print(cnt[0][0])
# 범위
print(nums[-1]-nums[0])

