from sys import stdin
input = stdin.readline

def solution(numbers):
  dp = [[0] * len(numbers) for _ in range(len(numbers) + 1)]
  for idx in range(len(numbers)):
    dp[0][idx] = 1

  for idx in range(1, len(numbers)):
    if numbers[idx - 1] == numbers[idx]:
      dp[1][idx] = 1
  
  for length in range(2, len(numbers)):
    for idx in range(length, len(numbers)):
      if dp[length - 2][idx - 1] == 1 and numbers[idx - length] == numbers[idx]:
        dp[length][idx] = 1
  
  return dp

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())

dp = solution(numbers)
ret = [0] * m
for i in range(m):
  s, e = map(int, input().split())
  ret[i] = dp[e - s][e - 1]
print(*ret, sep='\n')