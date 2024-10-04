import heapq as hq
from sys import stdin
input = stdin.readline

def solution(n, stations, cable):
  visited = [False] * (n + 1)
  min_val = [10000] * (n + 1)

  pq = []
  for station in stations:
    visited[station] = True
    for dst in cable[station]:
      hq.heappush(pq, dst)
  
  ret = 0; cnt = n - len(stations)
  while pq and cnt > 0:
    w, u = hq.heappop(pq)
    if visited[u]:
      continue
    ret += w
    cnt -= 1
    visited[u] = True
    for v_w, v in cable[u]:
      if not visited[v] and v_w < min_val[v]:
        hq.heappush(pq, (v_w, v))
        min_val[v] = v_w
  return ret

# input
n, m, k = map(int, input().split())
stations = list(map(int, input().split()))
cable = [[] for _ in range(n + 1)]
for i in range(m):
  u, v, w = map(int, input().split())
  cable[u].append((w, v))
  cable[v].append((w, u))
print(solution(n, stations, cable))