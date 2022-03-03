# 난이도 1.5
# (10)/20분 1초 128MB
'''
고정점 = arr[i] = i 인 수
오름차순 정렬된 수열 N개 원소 
고정점 출력. 없으면 01

제한 : O(logN)
'''
N = int(input())
nums = list(map(int,input().split()))

lo = 0
hi = len(nums)-1
answer = -1

def biggerThanReal(mid):
    if mid > nums[mid] :
        return 1
    elif mid < nums[mid]:
        return -1
    else : 
        return 0

while lo<=hi : # 돌면서
    mid = (lo+hi)//2
    if biggerThanReal(mid)>0:  # mid값(index값)이 실제데이터보다 크면
        lo = mid+1    # 오른쪽만 탐색 -> lo+1
    elif biggerThanReal(mid)<0:
        hi = mid-1
    else :
        answer = mid
        break
print(answer)