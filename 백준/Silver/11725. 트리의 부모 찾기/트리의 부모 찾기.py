import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list() for _ in range(n + 1)]

for _ in range(n - 1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(start):
  parents = [-1] * (n + 1)
  queue = deque([start])
  parents[start] = 0
  while queue:
    child = queue.popleft()
    for c in graph[child]:
      if parents[c] == -1:
        parents[c] = child
        queue.append(c)
  return parents

ret = bfs(1)
print(*ret[2:], sep='\n')