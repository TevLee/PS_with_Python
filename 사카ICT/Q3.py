import sys
input = sys.stdin.readline
w,h,D = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(D)]
MOD = 10000019

dp = [[0 for _ in range(255)] for _ in range(255)]

dp[0][0] # 개미문제 시작점
for i in range(w+1):
    for j in range(h+1):
        if i ==0 and j==0: #[0][0]초기화 덮어쓰기 방지
            continue
        dp[i][j]=0
        if i>0:
            dp[i][j] += dp[i-1][j]
        if j>0:
            dp[i][j] += dp[i][j-1]
        dp[i][j]%=MOD

ans = 0
for b in board:
    x, y = b
    # O -> A -> B -> X
    cntAB = (dp[x][y-1] * dp[w-x+1][h-y])%MOD

    # O -> A -> B -> X
    cntBA = (dp[x-1][y] * dp[w-x][h-y+1])%MOD

    ans += (cntAB+cntBA)%MOD
    ans %= MOD
print(ans)
