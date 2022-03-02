# 미로 탐색
from collections import deque

n,m = map(int,input().split())
board = [input() for _ in range(n)]
chk = [[False]*m for _ in range(n)]

dx = (0,1,0,-1)
dy = (1,0,-1,0)
def isValid(y,x):
    return 0<=y<n and 0<=x<m 
'''chk배열'''

def bfs():
    answer = n*m
    dq = deque()
    dq.append((0,0,1)) # 출발지+길이
    while dq: # bfs 돌면서
        y,x,l = dq.popleft()
        if y==n-1 and x==m-1 :
            # if l<answer :
            #     answer = l 
            return l # bfs이고 항상 이동가능하므로 현재 값을 리턴
        for i in range(4):# 상하좌우 체크해서 
            ny = y+dy[i]
            nx = x+dx[i]
            if isValid(ny,nx) and board[ny][nx] == '1' and not chk[ny][nx]: # 갈 수 있으면
                chk[ny][nx] = True # 방문하고
                dq.append((ny,nx,l+1)) # 삽입
    return answer

print(bfs())