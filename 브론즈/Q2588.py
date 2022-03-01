import sys
a = int(sys.stdin.readline())
b = sys.stdin.readline()
for i in range(2,-1,-1):
    print(a*int(b[i]))
print(a*int(b))
