import sys, heapq
input = sys.stdin.readline

t = int(input())
ret = []
for _ in range(t):
  k = int(input())
  costs = list(map(int,input().split()))
  heapq.heapify(costs)
  total = 0
  while len(costs) > 1:
    tmp = heapq.heappop(costs) + heapq.heappop(costs)
    total += tmp
    heapq.heappush(costs, tmp)
  ret.append(total)
print(*ret, sep='\n')