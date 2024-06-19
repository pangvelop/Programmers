def solution(strArr):
    result = [len(i) for i in strArr]
    tmp = []
    for i in set(result):
        tmp.append(result.count(i))
    
    return max(tmp)