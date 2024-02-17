from collections import deque
import sys
input = sys.stdin.readline

delta = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

m, n, h = map(int, input().split())
tomatos = [[list(map(int, input().split())) for i in range(n)] for j in range(h)]

queue = deque()
for z in range(h):
  for y in range(n):
    for x in range(m):
      if tomatos[z][y][x] == 1:
        queue.append([x, y, z])

while queue:
    x, y, z = queue.popleft()
    for dx, dy, dz in delta:
      x1 = x + dx
      y1 = y + dy
      z1 = z + dz
      if 0 <= x1 < m and 0 <= y1 < n and 0 <= z1 < h and tomatos[z1][y1][x1] == 0:
        queue.append([x1, y1, z1])
        tomatos[z1][y1][x1] = tomatos[z][y][x] + 1

ret = 0
for z in range(h):
  for y in range(n):
    for x in range(m):
      if tomatos[z][y][x] == 0:
        print(-1); exit(0)
      ret = max(ret, tomatos[z][y][x] - 1)
print(ret)
