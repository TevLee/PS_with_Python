# 골드 5
# 선 긋기 
# 1초 192MB
import sys
input = sys.stdin.readline
n = int(input()) # 100억
points = []
for _ in range(n):
    points.append(list(map(int,input().split())))
points.sort(key=lambda x: x[0])
s,e = points[0]
ans = 0

for i in range(1,n):
    if points[i][0] <= e <points[i][1]:# 일부만겹칠때
        e = points[i][1]# 선분을 연장
    elif points[i][0] > e : # 더 멀리서 시작할때 >> 선분추가
        ans += e-s # 구했던 선분길이 더해주고
        s,e = points[i] # 시작,종료점 수정
ans += e-s
print(ans)