def solution(todo_list, finished):
    result = []
    for i in range(len(finished)) :
        if int(finished[i]) == 0:
            result.append(todo_list[i])
    return result