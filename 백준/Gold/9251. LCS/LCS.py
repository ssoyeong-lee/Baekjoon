from sys import stdin

input = stdin.readline

s1 = list(input().rstrip())
s2 = list(input().rstrip())

dp = [0] * (len(s1))
for i, ss2 in enumerate(s2):
  lcs = 0
  for j, ss1 in enumerate(s1):
    if lcs < dp[j]:
      lcs = dp[j]
    elif ss1 == ss2:
      dp[j] = lcs + 1

print(max(dp))