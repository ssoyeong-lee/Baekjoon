from sys import stdin
import heapq as hq
input = stdin.readline

def solution(li):
  solved_pq = [] # cnt, deadline #len(solved_pq) == now
  pq = [[deadline, cnt * -1] for deadline, cnt in li]
  hq.heapify(pq)

  while pq:
    deadline, cnt = hq.heappop(pq)
    if len(solved_pq) >= deadline:
      hq.heappushpop(solved_pq, cnt * -1)
      continue
    hq.heappush(solved_pq, cnt * -1)
  return sum(solved_pq)

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
print(solution(li))