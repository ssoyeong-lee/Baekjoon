from sys import stdin
input = stdin.readline

def solution(a, b):
  a.sort(); b.sort()

  ret = 0
  i = j = 0
  tmp = 0
  while i < len(a) and j < len(b):
    if a[i] <= b[j]:
      ret += tmp
      i += 1
    else:
      tmp = j + 1
      j += 1

  if i != len(a):
    ret += (len(a) - i) * len(b)
  return ret

t = int(input())
ret = [0] * t
for i in range(t):
  input()
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  ret[i] = solution(a, b)
print(*ret, sep='\n')