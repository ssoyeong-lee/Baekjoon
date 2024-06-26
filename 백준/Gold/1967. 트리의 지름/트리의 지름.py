from sys import stdin
from collections import deque

input = stdin.readline

# input and preprocessing
n = int(input())

tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
	p, c, w = map(int, input().split())
	tree[p].append([c, w])
	tree[c].append([p, w])

# Get Tree Diameter
def bfs(start):
	visited = [False] * (n + 1)
	visited[start] = True
	ret = [start, 0]
	queue = deque([[start, 0]])
	
	while queue:
		now, dist = queue.popleft()
		ret = [now, dist] if dist > ret[1] else ret
		for nex, w in tree[now]:
			if not visited[nex]:
				visited[nex] = True
				queue.append([nex, dist + w])
	return ret

y, lenXY = bfs(1)
z, diameter = bfs(y)

# print result
print(diameter)
