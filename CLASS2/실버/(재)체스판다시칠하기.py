# 실버 V 
# https://www.acmicpc.net/problem/1018
# 풀이참고(220217)
n,m = map(int,input().split())
boards = [input() for _ in range(n)]
# 윗줄은 0 ~ m-8까지
# 아랫줄은 0 ~ n-8까지 돌면서, W일때B일때 각각 최소갯수 체크
min = 32 #최대 32개수정
for rowStart in range(n-7):
    for colStart in range(m-7):
        # 한번에 각각체크
        startW = 0 # 첫문자를 w로 생각
        startB = 0 # 첫문자를 B로 생각
        for i in range(rowStart,rowStart+8):
            for j in range(colStart,colStart+8):
                # 짝수일 때 # W면 sB+1, 아니면 sW+1
                if (i+j)%2 == 0:
                    if boards[i][j]!='W':
                        startW +=1
                    else :
                        startB +=1
                else : #홀수일 때 , W면 sW+1
                    if boards[i][j] != 'B':
                        startW +=1
                    else :
                        startB+=1
        # 최소값 수정
        if startW < min:
            min = startW
        elif startB < min:
            min = startB

print(min)
