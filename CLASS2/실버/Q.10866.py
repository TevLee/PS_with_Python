# 실버 4
# 덱
# 0.5초 256MB
'''

'''
from collections import deque
import sys
N = int(sys.stdin.readline())
dq = deque()
for _ in range(N):
    order = list(map(str,sys.stdin.readline().split()))
    if len(order)== 1:
        if order[0]=='pop_front':
            print( dq.popleft() if dq else -1)
        if order[0]=='pop_back':
            print( dq.pop() if dq else -1)
        elif order[0]=='size':
            print(len(dq))
        elif order[0]=='empty':
            print( 0 if dq else 1)
        elif order[0]=='front':
            print( dq[0] if dq else -1)
        elif order[0]=='back':
            print( dq[-1] if dq else -1)
    else : # push
        if order[0] == 'push_front':
            dq.insert(0,int(order[1]))
        if order[0] == 'push_back':
            dq.append(int(order[1]))