# 45656 -> 각 자릿수 숫자의 차이가 1
# 길이가 n인 계단 수가 총 몇개인지
N = int(input())
# dp[n][l] : 길이가 n일때 마지막수가 l인경우 계단수
dp = [[0 for _ in range(11)] for _ in range(110)]

for i in range(1,10):
    dp[1][i] = 1 # 길이가 1인 경우 마지막수가 i인 계단수 각 1개

for i in range(2,N+1):
    dp[i][0] = dp[i-1][1] # 길이가 i-1일때 끝자리가 1이면 i번째는 0이옴
    for j in range(1,10):
        # 길이가 i인 경우는 끝자리가 j+-1인경우
        dp[i][j] = (dp[i-1][j-1]+dp[i-1][j+1]) % 1000000000
sum = 0
for i in range(10):
    sum += dp[N][i] # 
print(sum%1000000000)



