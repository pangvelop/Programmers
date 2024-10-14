import sys

t = int(sys.stdin.readline())
for _ in range(t) :
  stack=[]
  list=sys.stdin.readline().rstrip()
  for i in list :
    if i == '(' :
      stack.append(i)
    elif i == ')' :
      if stack :
        stack.pop()
      else :
        print("NO")
        break
  else :
    if not stack :
      print("YES")
    else :
      print("NO")