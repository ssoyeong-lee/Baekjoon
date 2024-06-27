from sys import stdin

input = stdin.readline

s1 = list(input().rstrip())
s2 = list(input().rstrip())

dp = [0] * (len(s1) + 1)
for i, ss2 in enumerate(s2):
  prev = 0
  for j, ss1 in enumerate(s1):
    if ss1 == ss2:
      tmp = dp[j + 1]
      dp[j + 1] = prev + 1
      prev = tmp
    else:
      prev = dp[j + 1]
      dp[j + 1] = max(dp[j], dp[j + 1])

print(dp[-1])