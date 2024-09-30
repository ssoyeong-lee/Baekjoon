import heapq as hq
from sys import stdin
input = stdin.readline

def find(parent, x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]

def union(parent, i, j, rank):
  root_i = find(parent, i)
  root_j = find(parent, j)
  if root_i == root_j:
    return
  if rank[root_i] < rank[root_j]:
    parent[root_i] = root_j
    return
  else:
    parent[root_j] = root_i
    if rank[root_i] == rank[root_j]:
      rank[root_i] += 1

def change_cost_format(costs):
  ret = []
  for i in range(len(costs)):
    for j in range(i + 1, len(costs[i])):
      ret.append((costs[i][j], i, j))
  return sorted(ret)

# Kruskal
def solution(n, costs):
  parent = [i for i in range(n)]
  rank = [0] * n

  total = 0
  costs = change_cost_format(costs)
  for cost, i, j in costs:
    if find(parent, i) != find(parent, j):
      union(parent, i, j, rank)
      total += cost
  return total

# Prim
def solution2(n, costs):
  visited = [False] * n
  visited[0] = True

  min_val = [100000000] * n
  min_val[0] = 0

  pq = []
  for j in range(1, n):
    hq.heappush(pq, (costs[0][j], j))
  
  ret = 0; cnt = 0
  while pq and cnt != n - 1:
    cost, j = hq.heappop(pq)
    if visited[j] == True:
      continue
    ret += cost
    cnt += 1
    visited[j] = True
    for k in range(n):
      if not visited[k] and costs[j][k] < min_val[k]:
        hq.heappush(pq, (costs[j][k], k))
        min_val[k] = costs[j][k]
  return ret

#input 
n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
print(solution2(n, costs))