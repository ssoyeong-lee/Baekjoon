from collections import deque

def bfs(graph, visited, start):
    dq = deque([start])
    visited[start] = True
    
    while dq:
        cur = dq.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                dq.append(nxt)

def solution(n, computers):
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
    
    visited = [False] * n
    cnt = 0
    for i in range(n):
        if not visited[i]:
            bfs(graph, visited, i)
            cnt += 1
    return cnt
            