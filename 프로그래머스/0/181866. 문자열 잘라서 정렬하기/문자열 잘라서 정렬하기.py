def solution(myString):
    result = list(filter(None, myString.split("x")))
    return sorted(result)