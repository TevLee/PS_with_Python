# N*M 얼음틀 
# 총 아이스크림 갯수구하기
N,M = map(int,input().split())
board = [input() for _ in range(N)]
chk = [[False]*M for _ in range(N)]
dy = (-1,1,0,0)
dx = (0,0,-1,1)
answer = 0

def isValid(y,x):
    return 0<=y<N and 0<=x<M

'''DFS'''
def dfs(y,x):
    chk[y][x]=True                                  # 방문체크
    if board[y][x]=='0':                            # board를 input()으로 받아서 0이 아닌 '0'과 비교
        for i in range(4):                          # 상하좌우 돌면서
            ny = y+dy[i]
            nx = x+dx[i]
            if isValid(ny,nx) and not chk[ny][nx]:  # 유효성 검사  + 미체크확인
                dfs(ny,nx)                          # 재귀
''' Main함수 시작'''
for y in range(N):              # 모든 얼음틀 돌면서
    for x in range(M): 
        if chk[y][x] == False:  # 미방문시 dfs 시작 ([y,x]가 아이스크림 첫 얼음틀)  
            dfs(y,x)
            if board[y][x]=='0':# 미방문으로 dfs 돌았는데 '1'인 경우는 칸막이임
                answer +=1  
print(answer)