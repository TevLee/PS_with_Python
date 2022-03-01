from collections import deque
def solution(numbers, target):
    answer = 0
    dq = deque([(0,0)]) # 현재 숫자, 길이
    while dq:
        now = dq.popleft()
        if now[1]==len(numbers):# 길이가 numbers랑 같으면 체크하고 continue
            if now[0] == target:
                answer+=1
        else :
            plus = [now[0] + numbers[now[1]],now[1]+1]
            minus = [now[0] - numbers[now[1]],now[1]+1]
            dq.append(plus)
            dq.append(minus)
    return answer