import sys
input = sys.stdin.readline

n = int(input())
edges = [[False] * n for _ in range(n)]

tmp = list(map(int, input().split()))
root = 0
for i in range(n):
  if tmp[i] != -1:
    edges[i][tmp[i]] = edges[tmp[i]][i] = True
  else:
    root = i

target = int(input())

cnt = 0
visited = [False] * n 
def dfs(root):
  global cnt
  tag = True
  for child in range(n):
    if visited[child] == False and edges[root][child] == True and child != target:
      tag = False
      visited[child] = True
      dfs(child)
  if tag:
    cnt += 1

visited[root] = True
if target != root:
  dfs(root)

print(cnt)
