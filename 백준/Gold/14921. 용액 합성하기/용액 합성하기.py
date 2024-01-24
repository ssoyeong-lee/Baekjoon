from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
liqid = list(map(int, input().split()))

ret = set()
def binary_search(liqid, s, target):
    global set
    start = s
    end = len(liqid) - 1
    while start <= end:
        mid = (start + end) // 2
        if liqid[mid] > target:
            end = mid - 1
        elif liqid[mid] == target:
            return target
        else:
            start = mid + 1
    if start == s:
        return liqid[s]
    elif start == len(liqid):
        return liqid[end]
    return liqid[start] if abs(liqid[start] - target) < abs(liqid[end] - target) else liqid[end]

for i in range(n - 1):
    tmp = binary_search(liqid, i + 1, liqid[i] * -1)
    ret.add(liqid[i] + tmp)

li = list(ret)
li.sort()
print(binary_search(li, 0, 0))