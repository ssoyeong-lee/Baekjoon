from sys import stdin
input = stdin.readline

def solution(li, m):
  dp = [0] * len(li)
  dp[0] = li[0]
  cnt = [0] * m
  cnt[dp[0] % m] += 1
  for i in range(1, len(li)):
    dp[i] = dp[i - 1] + li[i]
    rest = dp[i] % m
    cnt[rest] += 1

  ret = cnt[0]
  for i in cnt:
    if i >= 2:
      ret += i * (i - 1) // 2
  return ret
  

n, m = map(int, input().split())
li = list(map(int, input().split()))
print(solution(li, m))