# 실버 4
# 나는야 포켓몬 이다솜
# 
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
mons = []
mons_dic = {}

for i in range(N):
    pk = input().rstrip()
    mons.append(pk)
    mons_dic[pk] = i+1

for _ in range(M):
    q = input().rstrip()

    if q.isdigit() : #숫자면
        print(mons[int(q)-1])
    else : # 문자열이면
        print(mons_dic[q])
        