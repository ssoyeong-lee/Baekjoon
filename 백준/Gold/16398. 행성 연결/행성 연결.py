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

#input 
n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, costs))