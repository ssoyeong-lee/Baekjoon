from bisect import bisect_right

def solution(scores):
    wanho = sum(scores[0])
    for i in range(1, len(scores)):
        if scores[0][0] < scores[i][0] and scores[0][1] < scores[i][1]:
            return -1


    scores.sort(key=lambda x:(-x[0], +x[1]))
    maxVal = scores[0][1]
    res = []
    for a, b in scores:
        if b >= maxVal:
            maxVal = b
            res.append(a + b)

    res.sort()

    
    return len(res) - bisect_right(res, wanho) + 1