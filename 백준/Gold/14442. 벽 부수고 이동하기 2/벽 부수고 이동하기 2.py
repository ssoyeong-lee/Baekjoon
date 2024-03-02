import sys
from collections import deque
input = sys.stdin.readline

delta = ((1, 0), (-1, 0), (0, 1), (0, -1))
BLANK = 0; WALL = 1

n, m, k = map(int, input().split())
board = [ list(map(int, input().rstrip())) for _ in range(n)] # 신기하구만
time = [[-1] * m for _ in range(n)]
cnt = [[-1] * m for _ in range(n)]

def bfs():
  global time, cnt

  q = deque([(0, 0)])
  time[0][0] = 1
  cnt[0][0] = 0

  while q:
    x, y = q.popleft()
    if (x, y) == (m - 1, n - 1):
      return time[y][x]
    
    # print(f'----- {x}, {y} ----')
    # print(*time, sep='\n')
    # print()
    # print(*cnt, sep='\n')

    for dx, dy in delta:
      x1, y1 = x + dx, y + dy
      if not (0 <= x1 < m and 0 <= y1 < n):
        continue

      if board[y1][x1] == BLANK and (cnt[y1][x1] == -1 or cnt[y1][x1] > cnt[y][x]):
        q.append((x1, y1))
        time[y1][x1] = time[y][x] + 1
        cnt[y1][x1] = cnt[y][x]
      elif board[y1][x1] == WALL and cnt[y][x] < k and (cnt[y1][x1] == -1 or cnt[y1][x1] > cnt[y][x] + 1):
        q.append((x1, y1))
        time[y1][x1] = time[y][x] + 1
        cnt[y1][x1] = cnt[y][x] + 1
  return -1

print(bfs())
