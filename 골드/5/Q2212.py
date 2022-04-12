#골드5
#센서
#2초 128MB
# 센서 n개 집중국 k개
# 집중국거리합이 최솟값
n = int(input()) # 1만
k = int(input()) # 1천
sensors = list(map(int,input().split()))
if n<=k:
    print(0)
else :
    sensors.sort()
    gaps = [ sensors[i]-sensors[i-1] for i in range(1,len(sensors))]
    gaps.sort()
    for _ in range(k-1):
        gaps.pop()
    print(sum(gaps))


