from sys import stdin

input = stdin.readline

s1 = list(input().rstrip())
s2 = list(input().rstrip())

dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

for y in range(1, len(s2) + 1):
  for x in range(1, len(s1) + 1):
    if s1[x - 1] == s2[y - 1]:
      dp[y][x] = dp[y - 1][x - 1] + 1
    else:
      dp[y][x] = max(dp[y - 1][x], dp[y][x - 1])

print(dp[-1][-1])