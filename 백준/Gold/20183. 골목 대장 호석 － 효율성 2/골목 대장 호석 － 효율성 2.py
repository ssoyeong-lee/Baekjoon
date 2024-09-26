import heapq as hq
from sys import stdin

input= stdin.readline

def solution(roads, a, b, c):
  li = [-1] * len(roads)
  li[a] = 0
  total = [-1] * len(roads)
  total[a] = 0

  pq = [(0, 0, a)]
  while pq:
    cur_max, cur_total, cur = hq.heappop(pq)
    if li[cur] != cur_max:
      continue
    for nxt_max, nxt in roads[cur]:
      val = max(nxt_max, cur_max)
      nxt_total = cur_total + nxt_max
      if (li[nxt] == -1 or li[nxt] > val) and nxt_total <= c:
        hq.heappush(pq, (val, nxt_total, nxt))
        li[nxt] = val
        total[nxt] = nxt_total
  return li[b]

n, m, a, b, c = map(int, input().split())
roads = [[] for _ in range(n + 1)]
for _ in range(m):
  u, v, cost = map(int, input().split())
  roads[u].append((cost, v))
  roads[v].append((cost, u))
print(solution(roads, a, b, c))