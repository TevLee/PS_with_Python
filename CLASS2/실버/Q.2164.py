# 실버 4 
# 카드 2
# 2초 128MB
'''
N장 카드(번호 1~N, 1이 가장위 N이 가장 아래)


'''
from collections import deque
N = int(input()) # 1~50만
dq = deque()
for i in range(1,N+1):
    dq.append(i)
for _ in range(N-1):# N-1번
        dq.popleft()# 하나빼고
        top = dq.popleft()# 하나빼서 뒤에 넣고
        dq.append(top)
print(dq.pop())
