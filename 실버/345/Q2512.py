# 실버3
# 예산
'''
4
120 110 140 150
485

127
'''
from bisect import bisect_left
N = int(input()) # 3~10000
yes = list(map(int,input().split())) # 예산 N개 1~10만
M = int(input()) #총예산 N~100억

lo = 0
hi = max(yes)


def is_possible(mid):
    return sum(min(ye,mid) for ye in yes) <= M # mid보다 작으면 필요예산,아니면 mid값 더한게 총예산(M)보다 작으면 True반환

while lo<=hi:
    mid = (lo+hi)//2
    '''if else에서 T/F를 판단하는 것이 Parametic Search이고 
    is_possible 내에서 2번째 알고리즘...문제 즉, 한문제에 두알고리즘'''
    if is_possible(mid): # 총예산 M보다 작으니까
        lo = mid+1 # low 값을 키운다
        ans = mid
    else:
        hi = mid-1
print(ans)
