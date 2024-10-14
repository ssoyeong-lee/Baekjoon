from sys import stdin
import heapq as hq
input = stdin.readline

def solution(pq):
  solved_pq = [] # cnt, deadline #len(solved_pq) == now
  pq.sort(key = lambda x:x[0])
  
  for i in range(len(pq)):
    deadline, cnt = pq[i]
    if len(solved_pq) >= deadline:
      hq.heappushpop(solved_pq, cnt)
      continue
    hq.heappush(solved_pq, cnt)
  return sum(solved_pq)

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
print(solution(li))