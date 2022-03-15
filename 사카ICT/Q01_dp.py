import sys

input = sys.stdin.readline
W = int(input())
weights = [1, 5, 10, 50, 100, 500]
costs = list(map(int,input().split()))
# 금액 * 동전종류(6) 크기만큼 2차원 배열선언
dp = [[0 for _ in range(W+1)] for _ in range(6)]

# 1원짜리 동전만 사용했을 때를 가정한 초기값
for i in range(W+1):
    dp[0][i] = costs[0]*i 

for k in range(1,6):
    for w in range(1,W+1):
        dp[k][w] = dp[k-1][w]
        if w-weights[k] >= 0 :
            # 아랫줄이 핵심
            dp[k][w] = min(dp[k][w],dp[k][w-weights[k]]+costs[k])

print(dp)