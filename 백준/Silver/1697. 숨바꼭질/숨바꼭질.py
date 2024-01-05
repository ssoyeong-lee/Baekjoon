from collections import deque

n, k = map(int, input().split())


li = [False] * 100001
def bfs(n, k):
  queue = deque()
  queue.append([n, 0])
  while queue:
    now, cnt = queue.popleft()
    if now == k:
      return cnt
    tmp = now + 1
    if 0<= tmp <= 100000 and not li[tmp]:
      queue.append([tmp, cnt + 1])
      li[tmp] = True
    tmp = now * 2
    if 0<= tmp <= 100000 and not li[tmp]:
      queue.append([tmp, cnt + 1])
      li[tmp] = True
    tmp = now - 1
    if 0<= tmp <= 100000 and not li[tmp]:
      queue.append([tmp, cnt + 1])
      li[tmp] = True

print(bfs(n, k))