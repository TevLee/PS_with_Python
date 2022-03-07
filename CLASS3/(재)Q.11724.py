# 실버 2
# 연결 요소의 갯수
# 3초 512MB
'''
무방향 그래프
정점 N개
간선 M개
'''
from collections import deque
import sys
N,M = map(int,input().split()) # 1~1000 0~N-1까지합
board = [[0]* (N+1)  for _ in range(N+1)]
chk = [False for _ in range(N+1)]
for _ in range(M):
    y,x = map(int, sys.stdin.readline().split())
    board[y][x]=board[x][y]=1
answer = 0
### BFS로 다시풀기