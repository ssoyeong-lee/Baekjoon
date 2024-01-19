import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

d = [[cost[0][0], cost[0][1], cost[0][2]]]
for i in range(1, n):
    r = cost[i][0] + min(d[i - 1][1] , d[i - 1][2])
    g = cost[i][1] + min(d[i - 1][0] , d[i - 1][2])
    b = cost[i][2] + min(d[i - 1][1] , d[i - 1][0])
    d.append([r, g, b])
print(min(d[-1]))