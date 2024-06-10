def solution(arr):
    result = []
    
    for i in range(len(arr)):
        if len(result) == 0:
            result.append(arr[i])
        else:
            if result[-1] == arr[i]:
                result.pop()
                i += 1
            elif result[-1] != arr[i]:
                result.append(arr[i])
                i += 1
    
    if len(result) == 0:
        return [-1]
    
    return result