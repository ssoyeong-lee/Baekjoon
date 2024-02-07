import sys, heapq
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
heapq.heapify(li)

for i in range(n - 1):
  tmp = list(map(int, input().split()))
  for t in tmp:
    if t > li[0]:
      heapq.heappushpop(li, t)


print(li[0])