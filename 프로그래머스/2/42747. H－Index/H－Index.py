def solution(citations):
    citations.sort()
    
    n = len(citations)
    hIndex = 0
    for h in range(1, max(citations) + 1):
        up = 0; down = 0
        for j in range(0, n):
            if citations[j] >= h:
                up += 1
            else:
                down += 1

        if up >= h:
            hIndex = max(hIndex, h)
    return hIndex