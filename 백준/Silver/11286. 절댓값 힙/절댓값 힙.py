from collections import defaultdict
import sys, heapq
input = sys.stdin.readline
n = int(input())

ret = []
hq = []
checker = defaultdict(int)
for _ in range(n):
  x = int(input())
  if x != 0:
    heapq.heappush(hq, abs(x))
    checker[x] += 1
  elif len(hq) == 0:
    ret.append(0)
  else:
    target = hq[0]
    if checker[target * -1] > 0:
      target *= -1
    ret.append(target)
    checker[target] -= 1
    heapq.heappop(hq)
print(*ret, sep='\n')