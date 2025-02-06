from sys import stdin
input = stdin.readline

def solution(s):
  stack = []
  cnt = 0
  is_laser = False
  for i in s:
    if not stack or i == '(':
      stack.append('(')
      is_laser = True
    else:
      stack.pop()
      if is_laser:
        cnt += len(stack)
      else:
        cnt += 1
      is_laser= False
  return cnt

print(solution(input().rstrip()))