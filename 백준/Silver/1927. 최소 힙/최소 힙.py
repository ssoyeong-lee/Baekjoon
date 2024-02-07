import sys, heapq

n = int(input())
hq = []; ret =[]
for _ in range(n):
  x = int(input())
  if x != 0:
    heapq.heappush(hq, x)
  elif len(hq) == 0:
    ret.append(0)
  else:
    ret.append(hq[0])
    heapq.heappop(hq)
print(*ret, sep='\n')