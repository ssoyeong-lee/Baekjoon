import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [list() for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
  a, b = map(int, input().split())
  edges[a].append(b)
  indegree[b] += 1

queue = deque()
for i in range(1, n + 1):
  if indegree[i] == 0:
    queue.append(i)

ret = []
while queue:
  cur = queue.popleft()
  ret.append(cur)
  for j in edges[cur]:
    indegree[j] -= 1
    if indegree[j] == 0:
      queue.append(j)

print(*ret)
