import heapq as hq
from sys import stdin
input = stdin.readline

def solution(n, m, cross):
  min_time = [-1] * (n + 1)
  visited = [0] * (n + 1)
  visited[1] = True
  pq = []
  for c in cross[1]:
    hq.heappush(pq, c)

  while pq:
    time, a = hq.heappop(pq)
    if a == n:
      return time + 1
    if visited[a]:
      continue
    visited[a] = True
    for nxt_time, b in cross[a]:
      if time % m <= nxt_time:
        nxt_time = time // m * m + nxt_time
      else:
        nxt_time = m * (time // m + 1) + nxt_time
      if not visited[b] and (min_time[b] == -1 or nxt_time < min_time[b]):
        hq.heappush(pq, (nxt_time, b))

  return -1


n, m = map(int, input().split())
cross = [[] for _ in range(n + 1)]
for i in range(m):
  a, b = map(int, input().split())
  cross[a].append((i, b))
  cross[b].append((i, a))
print(solution(n, m, cross))