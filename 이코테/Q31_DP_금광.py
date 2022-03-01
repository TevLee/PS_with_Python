# DP : 난이도 1.5
# 10:17 - (해답)
T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    golds = list(map(int,input().split()))
    dp = []
    idx = 0
    for _ in range(n):
        dp.append(golds[idx:idx+m])
        idx+=m
    # print(golds)
    # print(dp)
    for j in range(1,m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else :
                left_up = dp[i-1][j-1] #0,0

            if i == n-1:
                left_down = 0
            else :
                left_down = dp[i+1][j-1] #2,0
            left = dp[i][j-1] #1,0
            dp[i][j] += max(left,left_up,left_down)
    result = 0
    for i in range(n):
        result = max(result,dp[i][m-1]) # 0~n-1,m-1
    print(result)