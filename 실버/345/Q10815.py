# 실버 4
# 숫자 카드
# 숫자카드 N개
# M을 가지고 있는지 확인
'''
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10

1 0 0 1 1 0 0 1
'''
'''
2초 256MB
'''
N = int(input()) # 1~50만
nums = sorted(list(map(int,input().split()))) # -1000만 ~ 1000만
M = int(input()) # 1~50만
Mnums = list(map(int,input().split())) # 
ans = [0 for _ in range(M)]
# 입력
for i in range(len(Mnums)): #Mnums 돌면서
    target = Mnums[i]
    # 이분탐색하고
    lo = 0
    hi = N-1
    while lo<=hi:
        mid = (lo+hi)//2
        if nums[mid] < target:
            lo = mid+1
        elif nums[mid] > target:
            hi = mid-1
        else :
            ans[i] = 1
            break
print(ans)
print()
from bisect import bisect_left,bisect_right
ans2 = []
for i in range(len(Mnums)):
    ans2.append(1 if bisect_right(nums,Mnums[i])-bisect_left(nums,Mnums[i])!=0 else 0)
print(*ans2)
