# 난이도 2
# 2초 128MB
'''
높이 H
요청길이 M 
M만큼의 떡을 얻기 위해 설정할 수 있는 H의 최대값
'''
N,M = map(int,input().split()) # 떡 개수 N(1~100만), 떡 길이 M(1~200억)
cakes = list(map(int,input().split()))

lo = 0
hi = max(cakes)
answer = 0

def is_underM(mid):
    # cakes 돌면서 mid보다 큰값은 -mid 한 값을 더해준다. --> 이게 M이상이면 true
    tmp = 0
    for cake in cakes:
        tmp+= cake-mid if cake>mid else 0
    return True if tmp>=M else False

while lo<=hi: # 돌면서
    mid = (lo+hi)//2
    if is_underM(mid):  # 길이가 M이상이면
        lo = mid+1 # lo+1
        answer = mid
        # print(answer)
    else : # 길이가 M보다 작으면
        hi = mid-1 # hi-1

print(answer)