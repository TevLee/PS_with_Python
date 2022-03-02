n = int(input()) # 3<=n<=100
foods = list(map(int,input().split()))

dp = [0]*(n+1)
dp[1] = foods[0]
dp[2] = max(foods[1],foods[2])
for i in range(3,n+1):
    dp[i] = max(dp[i-1],dp[i-2]+foods[i-1])
print(dp[i])