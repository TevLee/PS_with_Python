# 2*n 크기의 직사각형을 1*2, 2*1로 채우기
n = int(input())
dp = [0 for _ in range(n+1)]

# dp[i] : 2*i일때 최대 타일 수
# 조건 1) 타일갯수가 동일
# 조건 2) 가로길이가 같다
# dp[i] = dp[i-1]+dp[i-2]
dp[1],dp[2] = 1,2
for i in range(3,n+1):
    dp[i] = (dp[i-1]+dp[i-2])%10007
print(dp[n])