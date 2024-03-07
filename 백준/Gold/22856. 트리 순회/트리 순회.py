import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
right = {}
for _ in range(n):
  a, b, c = map(int, input().split())
  if c != -1:
    right[a] = c

rightCnt = 0
def getRightLen(root):
  global rightCnt
  if root in right:
    rightCnt += 1
    getRightLen(right[root])

getRightLen(1)
print((n - 1) * 2 - rightCnt)