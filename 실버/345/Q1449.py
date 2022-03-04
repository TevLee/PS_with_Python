# 실버 3
# 수리공 항승
# 2초 128MB
'''
누수갯수 N개 
길이 L 테이프 
누수구멍 hole 좌우 0.5cm씩 막아야함
테이프 최소 갯수
'''
N,L = map(int,input().split()) # 1~1000
coord = [False] * 1001
for i in map(int,input().split()):
    coord[i] = True
answer = 0
# coord 앞에서부터 쭉 보면서
i = 0
while i <= 1000:
    if coord[i]==True:# True면 (테이프붙이기시작) 
        answer+=1# cnt+1
        if i+L < len(coord):
            for j in range(i+1,i+L):
                coord[j] = True# L-1길이까지 true하고
            i+=L
            continue
        else :
            break
    i+=1
print(answer)
'''
while i< 1001:
    if coord[i]: #i번째가 구멍이면
        ans +=1 
        x+=L     #테이브시작체크지점을 L만큼 옮기고
    else :
        x+1      #구멍아니면 다음칸확인
'''