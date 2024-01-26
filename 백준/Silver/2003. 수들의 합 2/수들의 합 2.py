import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.append(0)

st = 0; en = 1
tot = a[0]; cnt = 0
while en < len(a):
    if tot == m:
        cnt += 1
    if tot < m:
        tot += a[en]
        en += 1
    else:
        tot -= a[st]
        st += 1

print(cnt)