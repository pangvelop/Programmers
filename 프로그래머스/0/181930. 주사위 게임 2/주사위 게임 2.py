def solution(a, b, c):
    
    if a !=b and b!= c and a != c:
        return a+b+c
    elif a == b and b== c :
        return (3*a)*(3*a*a)*(3*a*a*a)
    else :
        return (a+b+c)*(a*a+b*b+c*c)