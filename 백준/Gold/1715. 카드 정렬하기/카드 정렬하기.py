import sys, heapq
input = sys.stdin.readline

n = int(input())
cards = []
for i in range(n):
  heapq.heappush(cards, int(input()))
if n == 1:
  print(0)
  exit(0)
else:
  ret = 0
  while len(cards) > 1:
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    ret += tmp
    heapq.heappush(cards, tmp)
  print(ret)
