# 난이도 2
# 50분 2초 128MB
'''
수직선 위에 N개 집(한 좌표에 여러 집X)
공유기 C개 설치

answer = 공유기 사이의 최대거리
'''
from itertools import combinations
N,C = map(int,input().split()) # 집 N(2~20만) # 공유기 C(2~N)
homes = []
for _ in range(N):
    homes.append(int(input()))
# 입력

selectHomes = list(combinations(homes,C))
answer = 0
for selHome in selectHomes:
    tmp = max(selHome) - min(selHome)
    for i in range(len(selHome)-1):
                      
        for j in range(i+1,len(selHome)):
            if abs(selHome[i]-selHome[j]) < tmp:
                tmp = abs(selHome[i]-selHome[j])
    if tmp > answer :
        answer = tmp
print(answer)