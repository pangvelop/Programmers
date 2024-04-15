def solution(num_list):
    answer = 0
    result = 1
    result2 = 0
    for i in num_list:
        result *= i
        result2 += i
    
    if result > result2**2:
        answer = 0
    else :
        answer =1
    return answer