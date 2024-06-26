import sys
from collections import deque

input = sys.stdin.readline

# input and preprocessing
n = int(input())
li = [[] for _ in range(n + 1)] 
for _ in range(n):
	tmp = list(map(int, input().split()))
	idx = 1; target = tmp[0]
	while tmp[idx] != -1:
		li[target].append([tmp[idx], tmp[idx + 1]])
		idx += 2

# get distance between each vertex
def bfs(start):
	ret = [start, 0]
	queue = deque([[start, 0]])
	visited = [False] * (n + 1)
	visited[start] = True

	while queue:
		prev, dist = queue.popleft()
		ret = [prev, dist] if dist > ret[1] else ret

		for now, w in li[prev]:
			if not visited[now]:
				queue.append([now, dist + w])
				visited[now] = True

	return ret

y, distXY = bfs(1)
z, diameter = bfs(y)

# print longest dist
print(diameter)