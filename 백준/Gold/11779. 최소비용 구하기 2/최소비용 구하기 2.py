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
      if costs[b] == -1 or costs[b] > tmp:
        costs[b] = tmp
        hq.heappush(pq, (tmp, b))
        prev[b] = a
  
  idx = e; cnt = 1; path = [e]
  while idx != s:
    idx = prev[idx]
    path.append(idx)
    cnt += 1
  path.reverse()
  return costs[e], len(path), path

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, cost = map(int, input().split())
  graph[a].append([b, cost])
s, e = map(int, input().split())
cost, cnt, path = solution(graph, s, e)
print(cost)
print(cnt)
print(*path)