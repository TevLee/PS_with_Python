#그룹단어
n = int(input())
cnt = 0
for i in range(n):
    words = input()
    dict = {}
    for j in range(len(words)):
        if words[j] not in dict:
            dict[words[j]] = 1
        else :
            if words[j-1] != words[j]:
                break
            else :
                dict[words[j]] +=1
    else :
        cnt+=1
    #print(dict)
print(cnt)
'''
N = int(input())
result = N
for i in range(0,N):
    word=input()
    for j in range(0,len(word)-1): #뒤에서 2번째 글자까지
        if word[j]==word[j+1]:  
            pass
        elif word[j] in word[j+1:]: #뒤알파벳과 다른데, 뒤에 또 있으면 == 따로 떨어진 두 알파벳이 있으면
            result-=1
            break
print(result)
'''