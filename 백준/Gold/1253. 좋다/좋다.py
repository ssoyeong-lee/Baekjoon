from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li.sort()

cnt = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        target = li[i] - li[j]
        right = bisect_right(li, target)
        left = bisect_left(li, target)
        tag = False
        for k in range(left, right):
            if k != i and k != j:
                tag = True
                break
        if tag:
            cnt += 1
            break
print(cnt)