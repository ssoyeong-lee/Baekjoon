import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

dp = [li[0]]
for i in range(1, n):
  if dp[-1] + li[i] < li[i]:
    dp.append(li[i])
  else:
    dp.append(li[i] + dp[-1])
print(max(dp))
