import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ret = [[0] * n for _ in range(n)]

def bfs(start, end):
  queue = deque([start])
  visited = [False] * n

  while queue:
    now = queue.popleft()
    if now == end and visited[now]:
      return 1
    for j in range(n):
      if arr[now][j] == 1 and not visited[j]:
        visited[j] = True
        queue.append(j)
  return 0

for i in range(n):
  for j in range(n):
    ret[i][j] = bfs(i, j)
  print(*ret[i])
