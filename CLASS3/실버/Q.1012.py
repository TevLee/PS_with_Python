# 실버 2
# 유기농 배추
# 1초 512MB
'''
배추 재배 -> 해충방지
1이 배추가 심어진 땅
>> Component count 문제
'''
import sys
sys.setrecursionlimit(10000)
T = int(input())
dy = [-1,1,0,0]
dx = [0,0,-1,1]
def is_inBoard(ny,nx):
    return 0<=ny<M and 0<=nx<N
def dfs(y,x):
    chk[y][x]=True #방문하고
    for i in range(4): # 상하좌우보고
        ny = y+dy[i]
        nx = x+dx[i]
        if is_inBoard(ny,nx) and board[ny][nx]==1 and not chk[ny][nx] :# 유효하고 & board1면
            # print(ny,nx)
            dfs(ny,nx)# 재귀

for _ in range(T):
    answer = 0
    ##1회당 코드##
    M,N,K = map(int,input().split()) # 가로,세로,배추갯수
    board = [[0]*N for _ in range(M)]
    chk = [[False]*N for _ in range(M)]
    for _ in range(K):
        y,x = map(int,input().split())
        board[y][x] = 1
    # 입력
    for j in range(N): # 전부 돌면서
        for i in range(M): 
            if board[i][j] == 1 and chk[i][j]==False:# board 1이고 미방문 chk=False면
                answer +=1 # answer +=1
                dfs(i,j)# dfs돈다
    #############
    print(answer)