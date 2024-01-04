import sys
import math
input = sys.stdin.readline

encoded = input().rstrip()
n = len(encoded)
max_num = math.ceil(n / 2)

max_val = [1, n]
for c in range(1, max_num + 1):
    for r in range(max_val[0] + 1, c + 1):
        if r * c == n:
            max_val = [r, c]
r, c = max_val

ret = ''
for i in range(r):
    for j in range(i, n, r):
        ret += encoded[ j]
print(ret)