import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

def bfs(f, s, g, u, d):
  queue = deque()
  queue.append((s, 0))
  visited = [False] * (f + 1)

  while queue:
    now, time = queue.popleft()
    if now == g:
      return time
    
    if now + u <= f and not visited[now + u]:
      queue.append((now + u, time + 1))
      visited[now + u] = True
    if now - d > 0 and not visited[now - d]:
      queue.append((now - d, time + 1))
      visited[now - d] = True
  return "use the stairs"

print(bfs(f, s, g, u, d))