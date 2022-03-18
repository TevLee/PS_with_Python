# 실버 1
# 회전초밥
# 1초 256MB
'''
https://www.acmicpc.net/problem/2531
8 30 4 30
7
9
7
30
2
7
9
25

5
'''
import sys
input = sys.stdin.readline
N,d,k,t = map(int,input().split())
# N : 총 초밥수
# d : 초밥 가짓수
# k : 가능한 연속 접시 수
# t : 쿠폰번호
v = list(int(input()) for _ in range(N))

# 슬라이드 윈도우
cnt, c = [0]*(d+1), 0 # cnt : 몇번초밥이 몇개있는지
for i in range(k):
    cnt[v[i]] +=1
    if cnt[v[i]] == 1 : 
        c+=1

# cnt[t]가 0아니면(즉, 쿠폰에 있는 초밥이 있으면) 
# 최대가능 갯수는 c+1
mx = c + (cnt[t]==0) 

# 투포인터
for i in range(N):
    cnt[v[i]] -= 1 # 1) 하나 줄이고
    if cnt[v[i]]== 0 : # 2) 줄여서 그 초밥이 0개면 총갯수에 하나빼고
        c -= 1
    cnt[v[(i+k)%N]] += 1 # 3) k번째 늘린다(% 는 원형이라서)

    if cnt[ v[(i+k)%N] ] == 1 : # 4) k번째가 0이었다가 1이되면 총갯수 +1
        c +=1
    mx = max(mx, c+(cnt[t]==0)) # 끝) 최대 갯수는 기존 vs. 현재 
print(mx)        
    