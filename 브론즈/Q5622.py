#A:65 Z:90
alphas = list(input())
num = 0
while len(alphas)>0:
    alpha = ord(alphas.pop(0))
    if alpha<=67:
        num+=2+1
    elif alpha<=70:
        num+=3+1
    elif alpha<=73:
        num+=4+1
    elif alpha<=76 :
        num+=5+1
    elif alpha<=79 :
        num+=6+1
    elif alpha<=83 :
        num+=7+1
    elif alpha<=86 :
        num+=8+1
    else :
        num+=9+1
    #print(num)
print(num)