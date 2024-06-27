from sys import stdin

input = stdin.readline

s1 = list(input().rstrip())
s2 = list(input().rstrip())

dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

for i, ss2 in enumerate(s2):
  for j, ss1 in enumerate(s1):
    if ss1 == ss2:
      dp[i + 1][j + 1] = dp[i][j] + 1
    else:
      dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
print(dp[-1][-1])