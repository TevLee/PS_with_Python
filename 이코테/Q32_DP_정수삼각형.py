#DP 난이도 1.5
#1:10
from inspect import trace
from random import triangular


n = int(input())
# height가 n인 삼각형 입력
dp = []
for i in range(n):
    row = list(map(int,input().split()))
    dp.append(row)

for i in range(1,n):
    for j in range(len(dp[i])):
        if j==0:
            left = dp[i-1][0]
        else :
            left = dp[i-1][j-1]
        if j==len(dp[i])-1:
            right = 0
        else:
            right = dp[i-1][j]
        dp[i][j] = dp[i][j]+max(left,right)
print(dp)
print(max(dp[n-1]))