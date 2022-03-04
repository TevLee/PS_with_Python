'''
10,50,100,500원 동전
800원 거스름돈 , 최소 사용
'''
money = 800
coins = [500,100,50,10]
answer = 0
for coin in coins:
    if money//coin >=1:
        answer += money//coin
        money %= coin
print(answer)