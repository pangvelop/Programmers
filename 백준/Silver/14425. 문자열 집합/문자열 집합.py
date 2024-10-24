import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
s = []
checklist=[]
count= 0
for _ in range(n) :
    s.append(sys.stdin.readline().rstrip())

for _ in range(m) :
    checklist.append(sys.stdin.readline().rstrip())

for i in checklist :
    if i in s :
        count += 1

print(count)