# import heapq as hq
from sys import stdin
input = stdin.readline

# def solution(n, stations, cable):
#   visited = [False] * (n + 1)
#   min_val = [10000] * (n + 1)

#   pq = []
#   for station in stations:
#     visited[station] = True
#     for dst in cable[station]:
#       hq.heappush(pq, dst)
  
#   ret = 0; cnt = n - len(stations)
#   while pq and cnt > 0:
#     w, u = hq.heappop(pq)
#     if visited[u]:
#       continue
#     ret += w
#     cnt -= 1
#     visited[u] = True
#     for v_w, v in cable[u]:
#       if not visited[v] and v_w < min_val[v]:
#         hq.heappush(pq, (v_w, v))
#         min_val[v] = v_w
#   return ret

# # input
# n, m, k = map(int, input().split())
# stations = list(map(int, input().split()))
# cable = [[] for _ in range(n + 1)]
# for i in range(m):
#   u, v, w = map(int, input().split())
#   cable[u].append((w, v))
#   cable[v].append((w, u))
# print(solution(n, stations, cable))

def find(parent, x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]

def union(parent, x, y, stations):
  root_x = find(parent, x)
  root_y = find(parent, y)
  if root_x == root_y:
    return
  if root_x in stations:
    parent[root_y] = root_x
  else:
    parent[root_x] = root_y

def solution(n, stations, cable):
  parent = [i for i in range(n + 1)]
  stations = set(stations)
  cable.sort(key=lambda x:x[2])

  ret = 0; cnt = n - len(stations)
  for u, v, w in cable:
    if cnt == 0:
      break
    root_u, root_v = find(parent, u), find(parent, v)
    if root_u == root_v or (root_u in stations and root_v in stations):
      continue
    union(parent, u, v, stations)
    ret += w
    cnt -= 1
  return ret

n, m, k = map(int, input().split())
stations = list(map(int, input().split()))
cable = [list(map(int, input().split())) for _ in range(m)]
print(solution(n, stations, cable))