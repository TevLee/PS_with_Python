# 실버 4
# 큐
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
        if order[0]=='pop':
            if dq: 
                print(dq.popleft())
            else :
                print(-1)
        elif order[0]=='size':
            print(len(dq))
        elif order[0]=='empty':
            print( 0 if dq else 1)
        elif order[0]=='front':
            print( dq[0] if dq else -1)
        elif order[0]=='back':
            print( dq[-1] if dq else -1)
    else : # push
        dq.append(int(order[1]))
