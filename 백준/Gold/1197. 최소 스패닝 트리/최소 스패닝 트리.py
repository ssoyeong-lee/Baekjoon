import heapq as hq
from sys import stdin
input = stdin.readline

#prim
def solution1(edges):
  visited = [False] * len(edges)
  visited[1] = True

  pq = []
  for w, v in edges[1]:
    hq.heappush(pq, (w, v))
  
  ret = 0
  while pq:
    w, v = hq.heappop(pq)
    if visited[v] == True:
      continue
    ret += w
    visited[v] = True
    for w1, v1 in edges[v]:
      if visited[v1]:
        continue
      hq.heappush(pq, (w1, v1))
  return ret

#input
v, e = map(int, input().split())
edges = [[] for _ in range(v + 1)]
for _ in range(e):
  a, b, c = map(int, input().split())
  edges[a].append((c, b))
  edges[b].append((c, a))
print(solution1(edges))