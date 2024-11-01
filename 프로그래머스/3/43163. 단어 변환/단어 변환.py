from collections import deque

def diff1(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
    return cnt == 1

def solution(begin, target, words):
    visited = [False] * len(words)
    
    dq = deque([[begin, 0]])
    while dq:
        cur, dist = dq.popleft()
        if cur == target:
            return dist

        for i in range(len(words)):
            if not visited[i] and diff1(cur, words[i]):
                dq.append([words[i], dist + 1])
                visited[i] = True
    return 0