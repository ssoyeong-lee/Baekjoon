def solution(n):
  dp = [[0] * 10 for _ in range(n + 1)]
  for i in range(1, n + 1):
    for j in range(10):
      if i == 1 or j == 9:
        dp[i][j] = 1
      elif j == 0:
        dp[i][j] = sum(dp[i - 1]) % 10007
      else:
        dp[i][j] = dp[i][j - 1] - dp[i - 1][j - 1]
  return sum(dp[-1]) % 10007

n = int(input())
print(solution(n))