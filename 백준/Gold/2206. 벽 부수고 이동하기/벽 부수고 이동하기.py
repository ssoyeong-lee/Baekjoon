import sys
from collections import deque

delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for i in range(n)]

def bfs():
  global visited
  queue = deque([(0, 0, 0)])
  visited[0][0][0] = 1

  while queue:
    x, y, cnt = queue.popleft()

    if (x, y) == (m - 1, n - 1):
      return visited[y][x][cnt]
    
    for dx, dy in delta:
      x1, y1 = x + dx, y + dy
      if not (0 <= x1 < m and 0 <= y1 < n):
        continue
      if board[y1][x1] == '0' and visited[y1][x1][cnt] == 0:
        visited[y1][x1][cnt] = visited[y][x][cnt] + 1
        queue.append((x1, y1, cnt))
      elif board[y1][x1] == '1' and cnt == 0:
        visited[y1][x1][1] = visited[y][x][0] + 1
        queue.append((x1, y1, 1))
  return -1

print(bfs())