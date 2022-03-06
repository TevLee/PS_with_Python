# 실버 2
# 회의실 배정
# 2초 128MB
'''
N개 회의
겹치지않는 최대 회의 갯수
'''
import sys
N = int(input()) # 1~10만
hs = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]# 입력받고
hs.sort(key=lambda x:x[0])# [0]기준으로 정렬먼저. 왜냐하면 --> [10,10] [9,10] 이 있을 경우, [9,10]이 먼저 회의해야 [10,10]도 할 수 있음
hs.sort(key=lambda x:x[1])# [1]기준으로 정렬
# 입력
time = hs[0][1]# time 첫번째 회의의 끝나는시간
answer = 1# answer =1
for i in range(1,N): # 1번째 인덱스부터 돌면서
    if hs[i][0] >= time: # 시작시작이 time보다 크면
        time = hs[i][1]# time을 이 회의의 끝나는 시간으로 수정
        answer +=1# answer+=1

print(answer)