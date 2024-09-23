from sys import stdin
import heapq as hq

input = stdin.readline

def solution(graph, s, e):
  pq = [(0, s)]
  costs = [-1] * len(graph)
  costs[s] = 0
  prev = [-1] * len(graph)
  prev[s] = 0
  
  while pq:
    cur_cost, cur_pos = hq.heappop(pq)
    if cur_cost > costs[cur_pos]:
      continue
    for next_pos, next_cost in graph[cur_pos]:
      tmp_cost = costs[cur_pos] + next_cost
      if costs[next_pos] == -1 or tmp_cost < costs[next_pos]:
        costs[next_pos] =tmp_cost
        hq.heappush(pq, (costs[next_pos], next_pos))
        prev[next_pos] = cur_pos

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
