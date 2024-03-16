import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
edges = [list() for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
	singers = list(map(int, input().split()))
	for i in range(1, len(singers) - 1):
		outVertex, inVertex = singers[i], singers[i + 1]
		if outVertex != inVertex:
			edges[outVertex].append(inVertex)
			indegree[inVertex] += 1

queue = deque()
for i in range(1, n + 1):
	if indegree[i] == 0:
		queue.append(i)

ret = []
while queue:
	cur = queue.pop()
	ret.append(cur)
	for node in edges[cur]:
		indegree[node] -= 1
		if indegree[node] == 0:
			queue.append(node)

if len(ret) == n:
	print(*ret, sep='\n')
else: print(0)