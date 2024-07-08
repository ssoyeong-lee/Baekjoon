from sys import stdin
from math import ceil

input = stdin.readline

n, k = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

stud = [[0] * 2 for _ in range(7)]
for l in li:
  gender, grade = l
  stud[grade][gender] += 1

ret = 0
for s in stud:
  w, m = s
  ret += ceil(w / k) + ceil(m / k)
print(ret)