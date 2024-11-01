def solution(brown, yellow):
    answer = []
    for w in range(yellow + 2, 2, -1):
        if yellow % (w - 2) != 0:
            continue
        h = yellow // (w - 2) + 2
        if brown == (w + h) * 2 - 4:
            return [w, h]
    return answer

# brown = (w + h) * 2 - 4
# yello = (w - 2) * (h - 2)