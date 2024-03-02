# import sys
# from collections import deque
# input = sys.stdin.readline

# BIAS = 10 ** 6
# delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# n, m = map(int, input().split())
# board = [input().rstrip() for _ in range(n)]
# visited = [[-1] * m for i in range(n)]

# def bfs():
#   global visited
#   visited[0][0] = 1

#   queue = deque()
#   queue.append((0,0))

#   while queue:
#     x, y = queue.popleft()
    
#     for dx, dy in delta:
#       x1 = x + dx; y1 = y + dy
#       if 0 <= x1 < m and 0 <= y1 < n:
#         if visited[y1][x1] == -1:
#           if board[y1][x1] == '0':
#             visited[y1][x1] = visited[y][x] + 1
#             queue.append((x1, y1))
#           elif board[y1][x1] == '1' and visited[y][x] <= BIAS:
#             visited[y1][x1] = visited[y][x] + 1 + BIAS
#             queue.append((x1, y1))
#         # elif board[y1][x1] == '0' and visited[y1][x1] % BIAS == visited[y][x] + 1:
#         #   visited[y1][x1] = visited[y][x] + 1

# bfs()
# # print(*visited, sep='\n')
# print(visited[-1][-1] % BIAS if not visited[-1][-1] == -1 else -1)

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
      if not (0 <= x1 < m and 0 <= y1 < n and visited[y1][x1][cnt] == 0):
        continue
      if board[y1][x1] == '0':
        visited[y1][x1][cnt] = visited[y][x][cnt] + 1
        queue.append((x1, y1, cnt))
      elif board[y1][x1] == '1' and cnt == 0:
        visited[y1][x1][1] = visited[y][x][0] + 1
        queue.append((x1, y1, 1))
  return -1

print(bfs())