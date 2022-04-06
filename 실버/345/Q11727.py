# 2*n 크기의 직사각형을 1*2, 2*1, 2*2로 채우기
n = int(input())
dp = [0 for _ in range(n+1)]

# dp[1] = 1, 2->3 , 3-> 5
# dp[i] = dp[i-1] + dp[i-2]*2
dp[1],dp[2] = 1,3
for i in range(3,n+1):
    dp[i] = (dp[i-1] + dp[i-2]*2)%10007
print(dp[n])
