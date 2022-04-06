# from collections import deque
# N,L = map(int,input().split())
# nums = list(map(int,input().split()))
# answers = []
# q = deque([nums[0]])
# idx = -L+1
# m = nums[0]

# while idx<0:# idx - 이면 첫수출력
#     answers.append(m)
#     idx+=1

# for i in range(1,L):# L-1개 넣고 시작
#     q.append(nums[i])
#     idx+=1
#     if nums[i] < m :
#         m = nums[i]
# for i in range(idx+1,N):
#     first = q.popleft()
#     q.append(nums[i])
#     if q[-1] < m:
#         m = q[-1]
#     elif first == m :
#         m = min(q)
#     answers.append(m)
# print(*answers)
from collections import deque 
n, l = map(int, input().split()) 
arr = [*map(int, input().split())] 
print(arr)
m = deque() 
for i in range(n): tmp = arr[i] 
while m and m[-1] > tmp: m.pop() 
m.append(tmp) 
#윈도우 크기보다 커진 단계에서 arr와 비교한 후 left pop 
if i >= l and m[0] == arr[i - l]: m.popleft() 
print(m[0], end=' ')
