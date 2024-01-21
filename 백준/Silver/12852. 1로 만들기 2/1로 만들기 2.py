n = int(input())

d = [[0, 0], [0, 0]]
for i in range(2, n + 1):
    tmp = []
    if i % 3 == 0:
        tmp.append([d[i // 3][0] + 1, i // 3])
    if i % 2 == 0:
        tmp.append([d[i // 2][0] + 1, i // 2])
    tmp.append([d[i - 1][0] + 1, i - 1])
    d.append(min(tmp, key=lambda x: x[0]))

i = n
ret = []
while i > 0:
    ret.append(i)
    i = d[i][1]
print(d[n][0])
print(*ret)