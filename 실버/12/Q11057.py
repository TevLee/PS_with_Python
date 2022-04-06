# 오르막수
N = int(input())
# dp[n][l] : 길이가 n이고 끝자리가 l인경우 오르막수
dp = [[0 for _ in range(11)] for _ in range(1001)]

# 초기화 : 길이가 1이고 끝자리가 i인 오르막수 1
for i in range(10):
    dp[1][i] = 1
# 점화식
for i in range(2,N+1):
   dp[i][0] = 1 # 길이가 i이고 끝자리가 0인 오르막수 1개 000...0
   for j in range(1,10):
       dp[i][j] = (dp[i][j-1]+dp[i-1][j])%10007
ans = 0
for i in range(10): #길이가 n이고 끝자리가 i인 오르막수
    ans += (dp[N][i])%10007
print(ans)