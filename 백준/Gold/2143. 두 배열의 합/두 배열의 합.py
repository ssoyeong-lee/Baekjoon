import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

t = int(input())
n = int(input())
liA = list(map(int, input().split()))
m = int(input())
liB = list(map(int, input().split()))

def sumLi(n, li):
    ret = []
    for i in range(n):
        tmp = 0
        for j in range(i, n):
            tmp += li[j]
            ret.append(tmp)
    ret.sort()
    return ret

sumA = sumLi(n, liA)
sumB = sumLi(m, liB)

if len(sumA) > len(sumB):
    tmp = sumA
    sumA = sumB
    sumB = tmp

cnt = 0
for a in sumA:
    target = t - a
    cnt += bisect_right(sumB, target) - bisect_left(sumB, target)
print(cnt)