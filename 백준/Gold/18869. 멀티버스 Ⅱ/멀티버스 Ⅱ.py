import sys
from collections import defaultdict

input = sys.stdin.readline

m, n = map(int, input().split())

ret = defaultdict(int)
for _ in range(m):
    li = list(map(int, input().split()))
    sortedLi = sorted(li)
    rank = {sortedLi[i]: i for i in range(len(sortedLi))}
    tmp = tuple([rank[i] for i in li])
    ret[tmp] += 1

cnt = 0
for i in ret.values():
    cnt += i * (i - 1) // 2
print(cnt)