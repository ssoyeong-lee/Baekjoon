from sys import stdin
input =stdin.readline

def solution(code):
  if code[0] == '0':
    return 0
  for c in code:
    if not '0' <= c <= '9':
      return 0
  if len(code) == 1:
    return 1

  dp = [0] * (len(code) + 1)
  dp[0] = 1
  dp[1] = 1

  for i in range(1, len(code)):
    num = int(code[i - 1: i + 1])
    if num == 10 or num == 20:
      dp[i + 1] = dp[i - 1]
    elif 10 < num <= 26:
      dp[i + 1] = (dp[i] + dp[i - 1]) % 1000000
    elif num % 10 != 0:
      dp[i + 1] = dp[i]
    else: 
      return 0

  return dp[-1]

code = input().rstrip()
print(solution(code))