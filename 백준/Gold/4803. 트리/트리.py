import sys
from collections import deque
input = sys.stdin.readline

def getGraph(data, root, visited):
  graph = set([root])
  queue = deque([root])
  visited.add(root)
  while queue:
    cur = queue.popleft()
    for nxt in data[cur]:
      if nxt not in visited:
        queue.append(nxt)
        visited.add(nxt)
        graph.add(nxt)
  return graph

def getEdgeCnt(data, graph):
  tmp = list(graph)
  cnt = 0
  for v in tmp:
    cnt += len(data[v])
  return cnt // 2

trees = []
while True:
  n, m = map(int, input().split())
  if (n, m) == (0, 0):
    break
  data = [list() for _ in range(n + 1)]
  for _ in range(m):
    u, v = map(int, input().split())
    data[u].append(v)
    data[v].append(u)
  
  visited = set()
  treeCnt = 0
  for root in range(1, n + 1):
    if root not in visited:
      graph = getGraph(data, root, visited)
      edgeCnt = getEdgeCnt(data, graph)
      if len(graph) - 1 == edgeCnt:
        treeCnt += 1
  trees.append(treeCnt)

ret = []
for idx in range(len(trees)):
  if trees[idx] == 0:
    ret.append(f'Case {idx + 1}: No trees.')
  elif trees[idx] == 1:
    ret.append(f'Case {idx + 1}: There is one tree.')
  else:
    ret.append(f'Case {idx + 1}: A forest of {trees[idx]} trees.')
print(*ret, sep='\n')