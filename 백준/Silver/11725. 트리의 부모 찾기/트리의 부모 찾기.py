from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
edge = [list() for _ in range(n + 1)]
for _ in range(n - 1):
  u, v = map(int, input().split())
  edge[u].append(v); edge[v].append(u)

parent = [-1] * (n + 1)
def bfs(root):
  queue = deque([root])
  parent[root] = 0
  while queue:
    p = queue.popleft()
    for child in edge[p]:
      if parent[child] == -1:
        parent[child] = p
        queue.append(child)

bfs(1)
print(*parent[2:], sep='\n')
