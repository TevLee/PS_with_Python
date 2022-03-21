# 브론즈 2
# 일곱난쟁이
# 2초 128MB
from itertools import combinations
heights = [int(input()) for _ in range(9)]
heights.sort()
for combi in combinations(heights,7):
    if sum(combi)==100:
        for i in range(7):
            print(combi[i])
        break