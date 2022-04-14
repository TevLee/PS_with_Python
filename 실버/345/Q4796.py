# 실버 5
# 캠핑
# 1초 128MB
# P일중 L일만 사용가능 V짜리 휴가 
# 1 < L < P < V
L,P,V = list(map(int,input().split()))
case = 1
while L+P+V != 0:
    # 20일 휴가... 캠핑장 8일중 5일 사용가능
    print("Case {0}: {1}".format(case,L * (V//P) + min(L,V%P)))
    L,P,V = list(map(int,input().split()))
    case+=1