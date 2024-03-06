import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def bfs(start):
  global visited
  queue = deque([start])

  while queue:
    now = queue.popleft()
    for j in range(n):
      if arr[now][j] == 1 and not visited[j]:
        visited[j] = 1
        queue.append(j)

ret = []
for i in range(n):
  visited = [0] * n
  bfs(i)
  print(*visited)
