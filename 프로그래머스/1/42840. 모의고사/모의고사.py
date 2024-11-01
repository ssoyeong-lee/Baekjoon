submitted = [[1, 2, 3, 4, 5], \
             [2, 1, 2, 3, 2, 4, 2, 5], \
             [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

def solution(answers):
    ret = [0] * len(submitted)
    for i in range(len(answers)):
        answer = answers[i]
        for j in range(len(submitted)):
            idx = i % len(submitted[j])
            if answer == submitted[j][idx]:
                ret[j] += 1
    max_score = max(ret)
    return [i + 1 for i in range(len(ret)) if ret[i] == max_score]