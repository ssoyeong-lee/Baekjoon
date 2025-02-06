from sys import stdin
input = stdin.readline

def solution(s):
  stack = []
  cnt = 0
  i = 0
  while i < len(s):
    if i + 1 < len(s) and s[i: i + 2] == '()':
      cnt += len(stack)
      i += 2
    elif not stack or s[i] == '(':
      stack.append('(')
      i += 1
    else:
      stack.pop()
      cnt += 1
      i += 1
  return cnt

s = input().rstrip()
print(solution(s))