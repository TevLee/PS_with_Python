import sys
input = sys.stdin.readline
N,M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = []

idx_a = 0
idx_b = 0
while idx_a < N and idx_b<M:
    if a[idx_a] > b[idx_b]:
        ans.append(b[idx_b])
        idx_b+=1
    else :
        ans.append(a[idx_a])
        idx_a+=1
ans += a[idx_a:] if idx_b==M else b[idx_b:]
print(*ans)
