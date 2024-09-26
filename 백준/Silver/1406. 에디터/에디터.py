from sys import stdin
from collections import deque

input = stdin.readline

def solution(line, command):
  left = deque(line)
  right = deque()

  for cmd in command:
    if cmd == 'D' and len(right) > 0:
      left.append(right.popleft())
    elif cmd == 'L' and len(left) > 0:
      right.appendleft(left.pop())
    elif cmd == 'B' and len(left) > 0:
      left.pop()
    elif cmd[0] == 'P':
      left.append(cmd.split()[1])
  return ''.join(left) + ''.join(right)

line = input().rstrip()
m = int(input())
cmd = [input().rstrip() for _ in range(m)]
print(solution(line, cmd))