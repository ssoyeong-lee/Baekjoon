import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
di = defaultdict(int)
for _ in range(n):
  di[int(input())] += 1
ret = list(di.items())
ret.sort(key=lambda x: (-x[1], x[0]))
print(ret[0][0])