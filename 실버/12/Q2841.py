# 실버 1
# 외계인의 기타 연주
# 1초 256MB
# 6개줄 p개 프렛
import heapq
from re import M
n,P = map(int,input().split()) # 50만, 30만
melodys = [ map(int,input().split()) for _ in range(n)]
ans = 0
# n개만큼 큐 만들기
lines = [[] for _ in range(n+1)] # 빈 리스트 n+1개
for m in melodys: # 멜로디하나씩 보면서
    ans+=1
    l,p = m
    if (-p,p) not in lines[l]: # 이미 플랫잡고 있으면 생략하되,
        heapq.heappush(lines[l],(-p,p)) # 플랫기준 최대힙만들고
    else : # 잡고있는거있으면 맨처음 ans를 상쇄
        ans-=1
    while lines[l][0] != (-p,p):  # 방금잡은 플랫나올때까지
        heapq.heappop(lines[l]) # 높은 플랫들 빼고
        ans+=1
print(ans)