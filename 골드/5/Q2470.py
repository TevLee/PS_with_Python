# 두용액
# 골드5
# 1초 128MB 
import sys

n = int(input()) # 2~10만
items = list(map(int,input().split()))
items.sort()
s,e=0,n-1
ans = sys.maxsize
ans_pos = [0,0]
while s<e:# 양끝에서 투포인터로 보면서
    tmp = items[s]+items[e]
    if abs(tmp) < ans :# 1)최솟값보다 작으면 업데이트
        ans = abs(tmp) ########################### 이것때문에 틀림
        ans_pos[0] = items[s]
        ans_pos[1] = items[e]
        if tmp == 0:# 4)0이면 끝낸다
            break
    if tmp<0: s+=1 # 2)s++ : 합이 음수일때
    else : e-=1 # 3)e-- : 합이 양수일때
    
print(*ans_pos)