import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
friends = [list() for _ in range(n + 1)]
while True:
  a, b = map(int, input().split())
  if (a, b) == (-1, -1):
    break
  friends[a].append(b)
  friends[b].append(a)

def bfs(start):
  visited = [-1] * (n + 1)
  visited[start] = 0
  queue = deque([start])
  while queue:
    now = queue.popleft()
    for f in friends[now]:
      if visited[f] == -1:
        visited[f] = visited[now] + 1
        queue.append(f)
  return max(visited     )

maxVal = 50
candidate = []
for i in range(1, n + 1):
  ret = bfs(i)
  if maxVal == ret:
    candidate.append(i)
  elif maxVal > ret:
    maxVal = ret
    candidate = [i]
print(maxVal, len(candidate))
print(*candidate)