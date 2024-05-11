def solution(n, slicer, num_list):
    result = []
    if n == 1 :
        result = num_list[0:slicer[1]+1]
    elif n == 2 :
        result = num_list[slicer[0]:]
    elif n == 3 :
        result = num_list[slicer[0]:slicer[1]+1]
    else :
        for i in num_list[slicer[0]:slicer[1]+1:slicer[2]] :
            result.append(i)
    return result