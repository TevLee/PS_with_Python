# 골드 5
# 배
# 2초 128MB
import sys
input = sys.stdin.readline

n = int(input()) # 50이하 자연수
containers = sorted(list(map(int,input().split())),reverse=True)
m = int(input()) # 박스수 1만 이하
boxes = sorted(list(map(int,input().split())),reverse=True)
#####
if containers[0] < boxes[0]:
    print(-1)
    sys.exit()
else :
    # 크레인이 들수 있는 가장 무거운 박스를 옮긴다
    # 모든 크레인 해결시 time+1
    time = 0
    while boxes:
        for c in containers:
            for box in boxes:
                if c >= box:
                    boxes.remove(box)
                    break
        time+=1
print(time)