def solution(n):
  size = max(n + 1, 5)
  dp = [0] * size
  dp[0] = 1
  dp[2] = 3
  for i in range(4, n + 1, 2):
    dp[i] = dp[i - 2] * 3
    for j in range(i - 4, -1, -2):
      dp[i] += dp[j] * 2
  return dp[n]

n = int(input())
print(solution(n))