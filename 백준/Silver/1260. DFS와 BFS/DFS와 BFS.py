import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
v, e, start = map(int, input().split())

# 인접 행렬 방식으로 구현
li = [[False] * (v + 1) for _ in range(v + 1)]
for i in range(e):
  v1, v2 = map(int, input().split())
  li[v1][v2] = li[v2][v1] = True

dfsRet = []
dfsVisited = [False] * (v + 1)
def dfs(now):
  dfsRet.append(now)
  dfsVisited[now] = True
  for i in range(1, v + 1):
    if li[now][i] and not dfsVisited[i]:
      dfsVisited[i] = True
      dfs(i)

bfsRet = []
bfsVisited = [False] * (v + 1)
def bfs(now):
  q = deque([now])
  bfsVisited[now] = True
  while q:
    node = q.popleft()
    bfsRet.append(node)
    for i in range(1, v + 1):
      if li[node][i] and not bfsVisited[i]:
        bfsVisited[i] = True
        q.append(i)

dfs(start); bfs(start)
print(*dfsRet)
print(*bfsRet)