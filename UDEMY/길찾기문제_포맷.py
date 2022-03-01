adj = [[0]*13 for _ in range(13)]
adj[0][1]=adj[0][7]=1
adj[1][2]=adj[1][5]=1
adj[2][3]=adj[2][4]=1
adj[5][6]==1
adj[7][8]=adj[7][9]=1
adj[9][10]=adj[9][11]=adj[9][12]=1

dy = (0,1,0,-1)
dx = (1,0,-1,0)
chk = [[False]* 13 for _ in range(13)] # 방문확인
N = int(input())

def isValid(y,x):
    return 0<=y<N and 0<=x<N
''' DFS '''
def dfs(y,x):
    chk[y][x] = True # 1) 방문체크
    for i in range(4): # 2) 상하좌우확인
        ny = y+dy[i]
        nx = x+dx[i]          
        if isValid(ny,nx) and not chk[ny][nx]: # 3) 유효성 & 방문확인
            dfs((ny,nx))

''' BFS '''
from collections import deque

def bfs(y,x):
    dq = deque()
    dq.append((y,x))
    while dq:
        y,x = dq.popleft()
        chk[y][x]=True      # 1) 방문체크
        for i in range(4):  # 2) 상하좌우확인
            ny = y+dy[i]
            nx = x+dx[i]
            if isValid(ny,nx) and not chk[ny][nx]: # 3) 유효성 & 방문확인
                dq.append((ny,nx))

