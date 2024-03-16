import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
names = input().rstrip().split()
names.sort()

edges = defaultdict(list)
indegree = defaultdict(int)

m = int(input())
for _ in range(m):
	x, y = input().rstrip().split()
	edges[y].append(x)
	indegree[x] += 1

root = []
for name in names:
	if indegree[name] == 0:
		root.append(name)

children = defaultdict(list)
for r in root:
	stack = deque([r])
	while stack:
		cur = stack.pop()
		for child in edges[cur]:
			indegree[child] -= 1
			if indegree[child] == 0:
				children[cur].append(child)
				stack.append(child)

for v in children.values():
	v.sort()

print(len(root))
print(*root)
for name in names:
	print(name, len(children[name]), *children[name])