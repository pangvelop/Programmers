def solution(numLog):
    result = []
    for i in range(len(numLog)-1) :
        if numLog[i+1]- numLog[i] ==1:
            result.append("w")
        elif numLog[i+1]- numLog[i] ==-1:
            result.append("s")
        elif numLog[i+1]- numLog[i] ==10:
            result.append("d")
        else  :
            result.append("a")
    return ''.join(result)