import sys
input = sys.stdin.readline

n = int(input())
lili = list(map(int, input().split()))

li = list(set(lili))
li.sort()

d = dict()
for l in range(len(li)):
    d[li[l]] = l

ret = []
for l in lili:
    ret.append(d[l])
print(*ret)