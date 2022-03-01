''' Breadth First Search'''
# Queue를 사용해서 구현
from collections import deque

''' 1. 인접행렬'''
adj = [[0]*13 for _ in range(13)]
adj[0][1]=adj[0][7]=1
adj[1][2]=adj[1][5]=1
adj[2][3]=adj[2][4]=1
adj[5][6]==1
adj[7][8]=adj[7][9]=1
adj[9][10]=adj[9][11]=adj[9][12]=1

def bfs():
    dq = deque()
    dq.append(0) # Root 노드 넣어주고
    while dq:
        now = dq.popleft()
        for nxt in range(len(adj[now])):
            if adj[now][nxt] == 1:
                dq.append(nxt)
                print("[%d] > [%d] 간선이 존재"%(now,nxt))

bfs()