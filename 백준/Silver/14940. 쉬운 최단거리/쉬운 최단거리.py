import sys
from collections import deque

input = sys.stdin.readline
delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

def bfs(startX, startY):
	queue = deque([[startX, startY]])
	while queue:
		x, y = queue.popleft()
		for dx, dy in delta:
			x1 = x + dx; y1 = y + dy
			if 0 <= x1 < m and 0 <= y1 < n and dist[y1][x1] == -1:
				if li[y1][x1] == 1:
					dist[y1][x1] = dist[y][x] + 1
					queue.append([x1, y1])

start = []
for y in range(n):
	for x in range(m):
		if li[y][x] == 2:
			start = [x, y]
			dist[y][x] = 0
		elif li[y][x] == 0:
			dist[y][x] = 0

bfs(*start)
for d in dist:
	print(*d)