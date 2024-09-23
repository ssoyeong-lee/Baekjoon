from sys import stdin
import heapq as hq

def solution(graph, s, e):
  pq = [(0, s)]
  costs = [-1] * len(graph)
  costs[s] = 0
  prev = [-1] * len(graph)
  prev[s] = 0
  
  while pq:
    cost, a = hq.heappop(pq)
    if cost > costs[a]:
      continue
    for b, c in graph[a]:
      tmp = costs[a] + c
      if costs[b] == -1 or tmp < costs[b]:
        costs[b] = tmp
        hq.heappush(pq, (costs[b], b))
        prev[b] = a

  idx = e; cnt = 1; path = [str(e)]
  while idx != s:
    idx = prev[idx]
    path.append(str(idx))
    cnt += 1
  path.reverse()
  return costs[e], len(path), ' '.join(path)

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, cost = map(int, input().split())
  graph[a].append([b, cost])
s, e = map(int, input().split())

print(*solution(graph, s, e), sep='\n')
