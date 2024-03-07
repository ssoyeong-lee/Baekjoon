import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, r, q = map(int, input().split())
edges = [list() for _ in range(n + 1)]
for _ in range(n - 1):
  u, v = map(int, input().split())
  edges[u].append(v)
  edges[v].append(u)
query = [int(input()) for _ in range(q)]

childCnt = [-1] * (n + 1)
def dfs(root):
  childCnt[root] = 1
  for child in edges[root]:
    if childCnt[child] == -1:
      dfs(child)
      childCnt[root] += childCnt[child]

dfs(r)
ret = []
for qr in query:
  ret.append(childCnt[qr])
print(*ret, sep='\n')