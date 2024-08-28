from sys import stdin
input = stdin.readline

def solution(n, costs):
  dp = [[0] * 3 for _ in range(n)]
  dp[0] = costs[0][:]; dp[0][2] += dp[0][1]
  dp[1][0] = dp[0][1] + costs[1][0]
  dp[1][1] = min(dp[0][1], dp[0][2], dp[1][0]) + costs[1][1]
  dp[1][2] = min(dp[0][1], dp[0][2], dp[1][1]) + costs[1][2]

  for i in range(2, n):
    dp[i][0] = min(dp[i - 1][:2]) + costs[i][0]
    dp[i][1] = min(*dp[i - 1], dp[i][0]) + costs[i][1]
    dp[i][2] = min(dp[i - 1][1], dp[i - 1][2], dp[i][1]) + costs[i][2]

  return dp[-1][1]

ret = []
while True:
  n = int(input())
  if n == 0:
    break
  costs = [list(map(int, input().split())) for _ in range(n)]
  ret.append(solution(n, costs))

for i in range(len(ret)):
  print(f'{i + 1}. {ret[i]}')