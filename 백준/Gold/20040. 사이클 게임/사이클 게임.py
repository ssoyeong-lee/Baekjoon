from sys import stdin
input = stdin.readline

def find(parent, x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]

def union(parent, x, y, rank):
  root_x = find(parent, x)
  root_y = find(parent, y)
  if root_x == root_y:
    return True
  if rank[root_x] < rank[root_y]:
    parent[root_x] = root_y
  else:
    parent[root_y] = root_x
    if rank[root_x] == rank[root_y]:
      rank[root_x] += 1
  return False

def solution(n, edges):
  parent = [i for i in range(n)]
  rank = [0] * n

  for idx in range(len(edges)):
    x, y = edges[idx]
    if union(parent, x, y, rank):
      return idx + 1
  return 0

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
print(solution(n, edges))