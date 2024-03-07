import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(n - 1):
  u, v, w = map(int, input().split())
  edges[u][v] = edges[v][u] = w

dist = [-1] * (n + 1)
depth = [-1] * (n + 1)
parent = [-1] * (n + 1)

def dfs(root):
  for child in range(1, n + 1):
    if edges[root][child] > 0 and dist[child] == -1:
      dist[child] = dist[root] + edges[root][child]
      depth[child] = depth[root] + 1
      parent[child] = root
      dfs(child)

dist[1] = depth[1] = parent[1] = 0
dfs(1)

def getGCP(u, v): # get Greatest Common Parent
  while u != v:
    if depth[u] > depth[v]:
      u = parent[u]
    else:
      v = parent[v]
  return u

ret = [0] * m
for i in range(m):
  u, v = map(int, input().split())
  gcp = getGCP(u, v)
  ret[i] = dist[u] + dist[v] - 2 * dist[gcp]

print(*ret, sep='\n')