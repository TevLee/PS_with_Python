# 실버 4
# 비밀번호 찾기
# 5초 256MB
'''
메모장에서 비밀번호를 찾아주는 프로그램
N 저장된 사이트 수
M 비밀번호 찾으려는 사이트 수
'''
import sys
N,M = map(int,input().split()) # 1~10만, 1~10만
infos = {}
for _ in range(N):
    site,pwd = map(str, sys.stdin.readline().split())
    infos[site] = pwd

for _ in range(M):
    site = sys.stdin.readline().rstrip()
    print(infos[site])