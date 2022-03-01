''' 1. 인접행렬'''
adj = [[0]*13 for _ in range(13)]
adj[0][1]=adj[0][7]=1
adj[1][2]=adj[1][5]=1
adj[2][3]=adj[2][4]=1
adj[5][6]==1
adj[7][8]=adj[7][9]=1
adj[9][10]=adj[9][11]=adj[9][12]=1

def dfs(now): #param 현재 방문하는 노드 
    for nxt in range(13):
        if adj[now][nxt]: # now --> nxt 존재하면
            print("[%d] > [%d]로 가는 간선이 존재합니다."%(now,nxt))
            dfs(nxt) # 재귀


dfs(0)      
