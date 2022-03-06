# 실버 4
# 팩토리얼 0의 갯수
# 2초 128MB
'''
N!에서 뒤에서 처음부터 0이 아닌 숫자가 나올때까지 0의 개수
'''
N = int(input()) # 0~500
answer = 0
for i in range(1,N+1): # N까지 5가 몇번 들어가면 되는가 (2는 당연히 5보다 많으니까)
    if i%5 == 0: # 5의 배수면 5가 몇번들어갔냐
        if i%125 == 0:
            answer +=3
        elif i%25 == 0:
            answer +=2
        else :
            answer +=1
print(answer)