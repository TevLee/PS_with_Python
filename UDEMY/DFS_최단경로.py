# 0 > 5 최단경로 찾기
adj = [[0]*13 for _ in range(13)]
adj[0][1]=adj[0][7]=1
adj[1][2]=adj[1][5]=1
adj[2][3]=adj[2][4]=1
adj[5][4]=adj[5][6]==1
adj[7][8]=adj[7][9]=1
adj[9][10]=adj[9][10]=adj[9][11]=adj[9][12]=1
adj[10][5]=1


def dfs(now,leng): #param 현재 방문하는 노드 
    if now == 5:
        print("5를 찾았습니다. 경로 길이는 %d 입니다"%(leng))
    for nxt in range(13):
        if adj[now][nxt]: # now --> nxt 존재하면
            dfs(nxt,leng+1) # 재귀


dfs(0,0)      
