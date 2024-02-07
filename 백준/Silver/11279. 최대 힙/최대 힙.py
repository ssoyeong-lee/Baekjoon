import sys
input = sys.stdin.readline

def heappush(li, x):
  li.append(x)
  now = len(li) - 1
  while now > 0:
    parent = (now - 1) // 2
    if li[now] > li[parent]:
      li[now], li[parent] = li[parent], li[now]
      now = parent
    else:
      break

def heappop(li):
  li[0], li[-1] = li[-1], li[0]
  del li[-1]
  
  now = 0
  while now * 2 + 2 < len(li):
    left = now * 2 + 1
    right = now * 2 + 2
    if li[left] >= li[right] and li[now] < li[left]:
      li[now], li[left] = li[left], li[now]
      now = left
    elif li[left] <= li[right] and li[now] < li[right]:
      li[now], li[right] = li[right], li[now]
      now = right
    else:
      break
  if now * 2 + 1 < len(li) and li[now] < li[now * 2 + 1 ]:
    li[now], li[now * 2 + 1] = li[now * 2 + 1], li[now]

n = int(input())
hq = []; ret = []
for i in range(n):
  x = int(input())
  if x != 0:
    heappush(hq, x)
  elif len(hq) == 0:
    ret.append(0)
  else:
    ret.append(hq[0])
    heappop(hq)
if len(ret) != 0:
  print(*ret, sep='\n')