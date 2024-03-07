import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(n - 1):
  u, v, w = map(int, input().split())
  edges[u][v] = edges[v][u] = w

def bfs(u, v):
  dist = [0] * (n + 1)
  queue = deque([u])
  while queue:
    cur = queue.popleft()
    if cur == v:
      break
    for child in range(1, n + 1):
      if dist[child] == 0 and edges[cur][child] > 0:
        dist[child] = dist[cur] + edges[cur][child]
        queue.append(child)
  return dist[v]

ret = [0] * m
for i in range(m):
  u, v = map(int, input().split())
  ret[i] = bfs(u, v)

print(*ret, sep='\n')