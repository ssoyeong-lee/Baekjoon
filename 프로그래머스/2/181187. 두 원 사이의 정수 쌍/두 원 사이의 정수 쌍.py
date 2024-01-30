import math
def solution(r1, r2):
    answer = 0
    for x1 in range(1, r2):
        val2 = math.floor(math.sqrt(r2 ** 2 - x1 ** 2))
        val1 = math.floor(math.sqrt(max(0, r1 ** 2 - x1 ** 2 - 1)))
        # answer += val2 - val1
        if val1 > 0:
            answer += val2 - val1
        else:
            answer += val2 + 1
        # print(val2, val1, answer)
    return (answer + 1) * 4
    
        