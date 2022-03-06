# 실버 4
# 듣보잡
# 2초 256MB
'''
듣도 못한 사람  N
보도 못한 사람  M
N,M에 각각 동명이인 없음
듣도 보도 못한 사람 ?(사전순 출력)
'''
import sys
N,M = map(int,input().split()) # 1~50만
answer = 0
answerList=[]
ns = set([sys.stdin.readline().rstrip() for _ in range(N)])
ms = set([sys.stdin.readline().rstrip() for _ in range(M)])
#입력
inter = sorted(list(ns&ms)) # SET의 교집합(&) -> LIST변환 -> 정렬
print(len(inter))
for item in inter:
    print(item)