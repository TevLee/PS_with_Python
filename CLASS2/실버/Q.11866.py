# 실버 4
# 요세푸스 문제 0
# 2초 512MB
'''
N명이 원으로 착석
N보다 작은 자연수 K
순서대로 K번째 사람 제거
제거되는 순서 --> 요세푸스 순열

ex) (7,3) -> <3,6,2,7,5,1,4>
'''
from collections import deque
N,K = map(int,input().split())
answer = deque()
dq = deque()
for i in range(1,N+1):
    dq.append(i)
# 입력
while dq: # dq 빌때까지
    for _ in range(K-1): # K-1개 빼서 뒤에넣고
        tmp = dq.popleft()
        dq.append(tmp)
    tmp = dq.popleft()# 하나 빼서 answer에 삽입
    answer.append(tmp)

print("<",end="")
for i in range(len(answer)-1):
    print(answer[i], end=", ")
print(str(answer.pop())+">")