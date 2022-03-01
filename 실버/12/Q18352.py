from collections import deque

n,m,k,x = map(int,input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    A,B = map(int,input().split())
    graph[A].append(B)

distance = [-1]*(n+1)
distance[x] = 0


q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node]== -1:
            distance[next_node] = distance[now]+1
            q.append(next_node)
#print(distance)
check = False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check = True
if check == False:
    print(-1)