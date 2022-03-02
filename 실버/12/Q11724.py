# 연결요소의 개수
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[0]*n for _ in range(n)]
visited = [False for _ in range(n)]
answer = 0
for _ in range(m):
    u,v = map(lambda x:x-1,map(int,input().split()))
    graph[u][v] = graph[v][u] = 1

def dfs(now): #now부터
    for nxt in range(n):
        if graph[now][nxt] and not visited[nxt]: # 연결된 노드가 미방문했으면
            visited[nxt]=True # 방문시키고
            dfs(nxt) #얘도 dfs돌림
for i in range(n): # 1) n개 노드 보면서
    if not visited[i]: # 방문안한 노드면
        answer +=1 # 연결요소 늘리고
        visited[i] = True #방문 시키고
        dfs(i) # 이 노드부터 dfs 돌려서 연결된 애들 다 방문
print(answer)
