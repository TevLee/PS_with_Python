# 실버 1
# 쿼드 트리
# 2초 128MB
'''
'''
def dfs(y,x,size):
    chk = board[y][x]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if board[j][i] != chk : #첫 수와 다르면
                chk = -1
                break
    if chk == -1: # 다르면 다시 쪼개고
        print("(",end="")
        dfs(y,x,size//2)
        dfs(y,x+size//2,size//2)
        dfs(y+size//2,x,size//2)
        dfs(y+size//2,x+size//2,size//2)
        print(")",end='')
    elif chk==1: # 모두 같은 수이면.... 그 수로 출력
        print(1,end='')
    else :
        print(0,end='')

N = int(input()) # 1,2,4,8,16,32,64
board = [list(map(int,input())) for _ in range(N)]
# 입력
dfs(0,0,N)