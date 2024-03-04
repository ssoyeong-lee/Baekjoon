import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
friends = [list() for _ in range(n + 1)]

for i in range(m):
  a, b = map(int, input().split())
  friends[a].append(b)
  friends[b].append(a)

def bfs():
  cnt = 0
  visited = [False] * (n + 1)

  queue = deque([[1, 0]])
  visited[1] = True
  while queue:
    now, dist = queue.popleft()
    for f in friends[now]:
      if not visited[f] and dist < 2:
        visited[f] = True
        cnt += 1
        queue.append([f, dist + 1])
  return cnt

print(bfs())
