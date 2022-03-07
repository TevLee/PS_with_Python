# 실버 3
# 2xn 타일링 2
# 1초 256MB
'''
2*n 직사각형을 1*2,2*1,2*2로 채우는 방법의 수
 1007로 나눈 나머지
점화식 n =[n-1]+2*[n-2] (n>=3)
'''
from collections import deque
n = int(input())
dp = deque([1,3])
for i in range(3,n+1):
    a = dp.popleft()
    dp.append((2*a+dp[0])%10007)
    # print(dp[0])
print(dp.pop())
