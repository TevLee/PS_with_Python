n,m = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
sorted(coins)
dp = [10001]*(m+1) # 0 ~ 가치의 합까지
dp[0]=0
for coin in coins:
    for j in range(coin,len(dp)):
        if dp[j-coin]!=10001:
            dp[j] = dp[j-coin]+1
if dp[m]==10001:
    print(-1)
else:
    print(dp[m])