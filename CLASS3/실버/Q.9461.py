# 실버 3
# 파도반 수열
# 1초 128MB
'''
삼각형이 나선모양으로 연속된 도형
첫 삼각형 변의 길이 1
가장 긴변이 k일때
파도반수열 P(N) : 정삼각형 변의 길이(오름차순)
N --> P(N)
'''
import sys
T = int(sys.stdin.readline())
pns = [0]*101
pns[1]=1
pns[2]=1
pns[3]=1
pns[4]=2
pns[5]=2
for _ in range(T):
    answer = 0
    num = int(input()) # num 받아서
    if num<=5:# 5이하면 그냥 출력
        print(pns[num])
    else :# 6이상이면
        for i in range(6,num+1):# 6~num까지 돌면서
            pns[i] = pns[i-1]+pns[(i-1)-4]### pns채우고
        print(pns[num])# pns[num]출력

'''
다른 풀이
1) i+3번째 숫자는 i번째 + i+3번째 숫자
'''