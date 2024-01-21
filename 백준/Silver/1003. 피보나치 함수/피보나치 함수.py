n = int(input())
li = [int(input()) for _ in range(n)]

m = max(li)
d = [[1, 0], [0, 1]]
for i in range(2, m + 1):
    d.append([d[-2][0] + d[-1][0], d[-2][1] + d[-1][1]])

for l in li:
    print(*d[l])
