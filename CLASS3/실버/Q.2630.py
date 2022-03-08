# 실버 3
# 색종이 만들기
# 1초 128MB
'''
NxN 크기 (N= 2^k : 1~7)
'''
'''
쿼드트리
'''
import sys
sys.setrecursionlimit(10000)
n = int(sys.stdin.readline()) # 2,4,8,16,32,64,128
board= [ list(map(int,sys.stdin.readline().split())) for _ in range(n) ]
white = 0 # 0
blue = 0 # 1

def func(x,y,size):
    global white, blue 
    chk = board[x][y] # 첫 인덱스 값 구하고
    for i in range(x,x+size):
        for j in range(y,y+size):
            if chk != board[i][j]:  # 첫 인덱스값과 다르면 재귀 다시 돌림
                func(x,y,size//2)
                func(x,y+size//2,size//2)
                func(x+size//2,y,size//2)
                func(x+size//2,y+size//2,size//2)
                return
    if chk == 0: #전부 0이면
        white += 1
        return
    if chk == 1:
        blue +=1
        return

#입력
func(0,0,n)
print(white)
print(blue)
