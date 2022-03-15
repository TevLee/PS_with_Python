# 4578
# 1 4 99 35 50 1000
# 1999
# 2 11 20 100 200 600
import sys

input = sys.stdin.readline
W = int(input())
weights = [1, 5, 10, 50, 100, 500]
costs = list(map(int,input().split()))

# 비율별로 정렬
jewels = list(zip(weights,costs))
jewels.sort(key=lambda x:x[1]/x[0])
ans = 0
# 적게 드는 비율 먼저 채우기
for w,c in jewels:
    cnt = W//w
    W %= w
    ans += cnt*c
print(ans)