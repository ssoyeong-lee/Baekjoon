from sys import stdin
input = stdin.readline

# input
t = int(input())
ret = [0] * t
for i in range(t):
  n, m = map(int, input().split())
  for _ in range(m):
    input()
  ret[i] = n - 1
print(*ret, sep='\n')