'''
도시 1~N 단방향 도로 M(거리 1)
X도시 -> K 거리의 (도달가능한)도시의 모든 번호
X->X : 거리 0
'''
from collections import deque
N,M,K,X = map(int,input().split()) # 도시, 도로, 거리정보, 출발도시
cities = [[0]*(N+1) for _ in range(M+1)]
roads = [list(map(int,input().split())) for _ in range(M)]
#print(roads)
lengs = [300000 for _ in range(N+1)]
for road in roads:
    cities[road[0]][road[1]] = 1
'''입력'''
dq = deque()
def bfs():
    while dq:
        y,x,l = dq.popleft()    # 큐에서 하나 빼고
        print("[%d %d %d]=%d"%(y,x,l, cities[y][x]))
        if cities[y][x]==1 :    # 값이 1이면 
            l+=1
            if lengs[x]>l:      # 길이가 짧으면
                lengs[x] = l    # 현재길이 배열에 넣고
            for i in range(1,N+1) : # 뒷자리 돌면서
                if cities[x][i] == 1:
                    dq.append((x,i,l))# 값이 1이면 큐에 넣기
'''반복문'''
for i in range(1,N):
    dq.append((X,i,0))
    bfs() # 시작노드 row bfs반복
print(lengs)
if K not in lengs:
    print(-1)
else :
    for i in range(1,len(lengs)):
        if lengs[i]==K:
            print(i)