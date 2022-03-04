# 실버 4
# 숫자 카드 2
# 1초 256MB
'''
N개 카드중
정수 M을 몇개씩 가지고 있나
'''
from bisect import bisect_left,bisect_right
N = int(input())
ns = sorted(list(map(int,input().split())))
M = int(input())
ms = list(map(int,input().split()))
# 입력
answer = [0] * M
for i in range(len(ms)):
    answer[i] = bisect_right(ns,ms[i]) - bisect_left(ns,ms[i])
print(*answer)

