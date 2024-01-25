from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = [int(input()) for _ in range(n)]
li.sort()


minVal = set()
for i in range(n - 1):
    target = m + li[i]
    left = bisect_left(li, target, i + 1)
    if left != len(li):
        minVal.add(li[left] - li[i])

print(min(minVal))