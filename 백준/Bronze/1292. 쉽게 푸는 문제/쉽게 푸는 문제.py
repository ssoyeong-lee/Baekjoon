a, b = map(int, input().split())

dp = [0]
n = 1
while len(dp) - 1 < b:
  dp += [n] * n
  n += 1
print(sum(dp[:b + 1]) - sum(dp[:a]))