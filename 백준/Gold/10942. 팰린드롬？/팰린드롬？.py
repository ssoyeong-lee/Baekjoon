from sys import stdin
input = stdin.readline

def solution(numbers, query):
  dp = [[False] * len(numbers) for _ in range(len(numbers))]
  for length in range(len(numbers)):
    for idx in range(length, len(numbers)):
      if length == 0:
        dp[length][idx] = True
      elif length < 2 and numbers[idx - 1] == numbers[idx]:
        dp[length][idx] = True
      elif dp[length - 2][idx - 1] == True and numbers[idx - length] == numbers[idx]:
        dp[length][idx] = True
  
  ret = [0] * len(query)
  for i in range(len(query)):
    s, e = query[i]
    if dp[e - s][e - 1]:
      ret[i] = 1
  return ret

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
query = [list(map(int, input().split())) for _ in range(m)]

ret = solution(numbers, query)
print(*ret, sep='\n')