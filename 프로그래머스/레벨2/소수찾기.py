#08:48~
import itertools
def is_prime(x):
    for i in range(2,x):
        if x%i ==0:
            return False
    return True
def solution(numbers):
    answer = 0
    per=[]
    for i in range(1,len(numbers)+1):
        tmp=list(map("".join(itertools.permutations(numbers,i))))
        tmp = int(tmp)
        per.append(tmp)
    for num in per:
        if is_prime(num): answer+=1
    return answer