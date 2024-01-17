import sys
input = sys.stdin.readline

n = int(input())
step = [int(input()) for _ in range(n)]
if n == 1:
    print(step[0])
    exit(0)

d = [[0 , 0], [step[0], 0], [step[0] + step[1], step[1]]]

for i in range(3, n + 1):
    d.append([d[i - 1][1] + step[i - 1], max(d[i - 2]) + step[i - 1]])
print(max(d[n]))