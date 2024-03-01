import sys
from collections import deque
input = sys.stdin.readline

def input_building(l, r, c):
  ret = []
  for z in range(l):
    tmp = []
    for y in range(r):
      tmp.append(input().rstrip())
    ret.append(tmp)
    input()
  return ret

def find_start(building, l, r, c):
  for z in range(l):
    for y in range(r):
      for x in range(c):
        if building[z][y][x] == 'S':
          return (x, y, z, 0)

def bfs(building, l, r, c):
  start_point = find_start(building, l, r, c)
  queue = deque()
  queue.append(start_point)

  visited = [[[False] * c for _ in range(r)] for __ in range(l)]
  visited[start_point[2]][start_point[1]][start_point[0]] = True

  while queue:
    x, y, z, t = queue.popleft()
    if building[z][y][x] == 'E':
      return f'Escaped in {t} minute(s).'

    for dx, dy, dz in delta:
      x1 = x + dx
      y1 = y + dy
      z1 = z + dz
      if 0 <= x1 < c and 0 <= y1 < r and 0 <= z1 < l:
        if not building[z1][y1][x1] == '#' and not visited[z1][y1][x1]:
          queue.append((x1, y1, z1, t + 1))
          visited[z1][y1][x1] = True
  return 'Trapped!'

delta = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
ret = []

while True:
  l, r, c = map(int, input().split())
  if l == 0 and r == 0 and c == 0:
    break
  building = input_building(l, r, c)
  ret.append(bfs(building, l, r, c))

print(*ret, sep='\n')