t = int(input())
for i in range(0,t) :
    iter, str = input().split()
    for j in str :
        print(j*int(iter), end='')
    print()