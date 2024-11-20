lst=[]
for _ in range(5) :
    a =int(input())
    if a <=40 :
        a=40
    lst.append(a)

print(int(sum(lst)/5))