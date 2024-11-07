def solution(arr):
    min_value = min(arr)
    ret = []
    for a in arr:
        if a != min_value:
            ret.append(a)
    return ret if ret else [-1]