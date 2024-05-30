def solution(myString):
    result =[]
    split = myString.split('x')
    for i in range(len(split)) :
        result.append(len(split[i]))
    return result