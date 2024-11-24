import sys

s = sys.stdin.readline().rstrip()

lst= set()

for i in range(0, len(s)) :
    for j in range(0, len(s)) :
        lst.add(s[i:j+1])

print(len(lst)-1)