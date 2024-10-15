from sys import stdin
from collections import deque
input = stdin.readline

def solution(ladder, snake):
  dist = [-1] * 101
  dist[1] = 0
  dq = deque([1])
  while dq:
    cur = dq.popleft()
    if cur == 100:
      return dist[100]
    for dx in range(1, 7):
      nxt = cur + dx
      if nxt in ladder:
        nxt = ladder[nxt]
      elif nxt in snake:
        nxt = snake[nxt]
      if nxt <= 100 and dist[nxt] < dist[cur]:
        dist[nxt] = dist[cur] + 1
        dq.append(nxt)
  return -1

n, m = map(int, input().split())
ladder = {}; snake = {}
for _ in range(n):
  a, b = map(int, input().split())
  ladder[a] = b
for _ in range(m):
  a, b = map(int, input().split())
  snake[a] = b

print(solution(ladder, snake))