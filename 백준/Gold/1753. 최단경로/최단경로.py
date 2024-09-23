from sys import stdin
import heapq as hq
input = stdin.readline

def solution(edges, start):
  uncert = []
  hq.heappush(uncert, (0, start))

  dist = [-1] * (len(edges))
  dist[start] = 0
  
  while uncert:
    minDist, minV = uncert[0]
    hq.heappop(uncert)
    if minDist > dist[minV]:
      continue
    for v, w in edges[minV]:
      if dist[v] == -1 or dist[v] > dist[minV] + w:
        dist[v] = dist[minV] + w
        hq.heappush(uncert, (dist[v], v))
  return dist[1:]

cntV, cntE = map(int, input().split())
start = int(input())
edges = [[] for _ in range(cntV + 1)]
for _ in range(cntE):
  u, v, w = map(int, input().split())
  edges[u].append([v, w])
dist = solution(edges, start)
ret = [d if d != -1 else 'INF' for d in dist]
print(*ret, sep='\n')