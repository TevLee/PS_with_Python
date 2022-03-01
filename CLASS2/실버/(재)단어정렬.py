# 실버 5
# https://www.acmicpc.net/problem/1181
# 풀이 참고
import sys
n = int(input())
words = [sys.stdin.readline().strip() for _ in range(n)]

# key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬한다.
setted = list(set(words))
setted.sort()
setted.sort(key=lambda x:len(x))

for word in setted:
    print(word)
