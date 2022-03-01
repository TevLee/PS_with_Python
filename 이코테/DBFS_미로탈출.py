''' 
N*M 미로 
현재 위치 (1,1)
괴물 0 빈칸 1
반드시 탈출 가능
탈출위한 최소 칸 개수
'''
from collections import deque
N,M = map(int,input().split())
maze = [input() for _ in range(N)]
chk = [[False]*M for _ in range(N)]
dy = (-1,1,0,0)
dx = (0,0,-1,1)
min = N*M

def isValid(y,x):
    return 0<=y<N and 0<=x<M

dq = deque([(0,0,0)]) # (0,0)넣고
while dq:#while dq
    y,x,l = dq.popleft()# 하나 pop해서
    chk[y][x]# 방문하고
    l+=1
    if y==N-1 and x==M-1: ### 종료지점 : 도착지면 ###
        print("정답은 %d"%(l))# print --> break
        break
    for i in range(4):#상하좌우보면서
        ny = y+dy[i]
        nx = x+dx[i]
        if isValid(ny,nx) and maze[ny][nx]=='1' : #유효성 및 1인지체크
            dq.append((ny,nx,l))#넣는다





