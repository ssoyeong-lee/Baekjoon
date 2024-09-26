from sys import stdin
import heapq as hq

input = stdin.readline

MAX_VAL = 100000 * 100000


def solution(roads, place):
  li = [MAX_VAL] * len(roads)
  pq = []
  for p in place:
    li[p] = 0
    hq.heappush(pq, (0, p))

  while pq:
    cur_dist, cur = hq.heappop(pq)
    if li[cur] != cur_dist:
      continue
    for nxt_dist, nxt in roads[cur]:
      dist = nxt_dist + cur_dist
      if li[nxt] > dist:
        hq.heappush(pq, (dist, nxt))
        li[nxt] = dist
  
  ret_idx, ret_val = 1, li[1]
  for i in range(2, len(li)):
    if ret_val < li[i]:
      ret_idx, ret_val = i, li[i]
  return ret_idx, ret_val

#input
n, m, k = map(int, input().split())
roads = [[] for _ in range(n + 1)]
for _ in range(m):
  u, v, c = map(int, input().split())
  roads[v].append((c, u))
place = list(map(int, input().split()))

# result
print(*solution(roads, place), sep='\n')