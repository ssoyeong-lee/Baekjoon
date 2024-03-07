import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
left = {}; right = {}
for _ in range(n):
  a, b, c = map(int, input().split())
  if b != -1:
    left[a] = b
  if c != -1:
    right[a] = c

cnt = 0 
def solve(root):
  global cnt
  if root in left:
    cnt += 2
    solve(left[root])
  if root in right:
    cnt += 2
    solve(right[root])


rightCnt = 0
def getRightLen(root):
  global rightCnt
  if root in right:
    rightCnt += 1
    getRightLen(right[root])

solve(1)
getRightLen(1)
print(cnt - rightCnt)