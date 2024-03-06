import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
friends = [list() for _ in range(n + 1)]

for i in range(m):
  a, b = map(int, input().split())
  friends[a].append(b)
  friends[b].append(a)

ret = [0] * (n + 1)

def bfs(start):
  visited = [-1] * (n + 1)
  visited[start] = 0
  queue = deque([start])
  while queue:
    person = queue.popleft()
    for f in friends[person]:
      if visited[f] == -1:
        queue.append(f)
        visited[f] = visited[person] + 1
  # print(visited, sum(visited) + 1)
  return sum(visited) + 1

answer = 1
theNumber = bfs(1)
for i in range(2, n + 1):
  tmp = bfs(i)
  if theNumber > tmp:
    theNumber = tmp
    answer = i
print(answer)
