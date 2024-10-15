from sys import stdin
input = stdin.readline

def solution(s, q):
  dp = [[0]* 26]
  for c in s:
    dp.append(dp[-1][:])
    dp[-1][ord(c) - ord('a')] += 1
  
  ret = []
  for c, s, e in q:
    s, e = int(s) + 1, int(e) + 1
    idx = ord(c) - ord('a')
    ret.append(dp[e][idx] - dp[s - 1][idx])
  return ret

s = input().rstrip()
n = int(input())
q = [input().split() for _ in range(n)]
print(*solution(s, q), sep='\n')