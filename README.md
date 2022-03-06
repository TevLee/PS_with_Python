# PS_with_Python
Problem solve using python

# 집합 SET
```
# 선언
s1 = set({1,2,3})
s2 = {3,4,5}

# 기본 메서드
s1.add(4) # s1에 4추가
s1.update({5,6}) # s1에 여러개(5,6)추가
s1.remove(6) # s1에 6제거(값이 없으면 오류발생)
s1.discard(5) # s1에 5 안전하게 제거(값이 없으면 아무일도 일어나지 않음)
s1.pop(4) # s1에 4제거
s1.clear() # s1 비우기
print(1 in s1) # 1이 s1에 있는지 확인

# 교집합
print(s1.intersection(s2)) #
print(s1 & s2)

# 합집합
print(s1.unison(s2)) #
print(s1 | s2)

# 차집합 
print(s1.difference(s2))
print(s1 - s2)

print(s2.difference(s1))
print(s2 - s1)

# 같은지 확인
print(s1 == s2)

# 완전히 다른지 (교집합이 없는지)
print(s1.isdisjoint(s2))

```
