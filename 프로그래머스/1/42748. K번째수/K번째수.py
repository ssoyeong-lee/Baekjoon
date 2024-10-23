def solution(array, commands):
    ret = []
    for i, j, k in commands:
        ret.append(sorted(array[i - 1: j])[k - 1])
    return ret
        