# 3273 - 두 수의 합 `silver 3`
import sys

def bisect(li, n, st, en):
  while st <= en:
    mid = (st + en) // 2
    if li[mid] == n:
      return True
    elif li[mid] > n:
      en = mid - 1
    else:
      st = mid + 1
  return False

n = int(input())
li = list(map(int, input().split()))
li.sort()
x = int(input())

ret = 0
for i in range(n - 1):
  target = x - li[i]
  if bisect(li, target, i + 1, n - 1):
    ret += 1
print(ret)
