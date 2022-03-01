words = input()
li = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in li:
    words = words.replace(i,"*")
print(len(words))