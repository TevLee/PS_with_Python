n,m = map(int,input().split())
board = [ list(input()) for _ in range(n) ]
ans = 64

def white_board(sy,sx):
    diff_cnt = 0
    for y in range(8):
        for x in range(8):
            if (y+x)%2 == 0:
                chk = 'W'
            else : 
                chk = 'B'
            if board[sy+y][sx+x] != chk:
                diff_cnt +=1 
    return diff_cnt
def black_board(sy,sx):
    diff_cnt = 0
    for y in range(8):
        for x in range(8):
            if (y+x)%2 != 0:
                chk = 'W'
            else : 
                chk = 'B'
            if board[sy+y][sx+x] != chk:
                diff_cnt +=1 
    return diff_cnt
# 0,0 -> m-8,n-8까지 가능
for y in range(n-7): # 시작점 중심으로 8*8 봤을 때
    for x in range(m-7):
        # print(y,x)
        w_ans = white_board(y,x)# 각 board와 다른 것 갯수 체크
        b_ans = black_board(y,x)# 각
        ans = min(ans,min(w_ans,b_ans))# ans 보다 작으면 업데이트
print(ans)