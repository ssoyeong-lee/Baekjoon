n = int(input())

d = [[0, 0] for _ in range(n + 1)]
for i in range(2, n + 1):
    d[i] = [d[i - 1][0] + 1, i - 1]
    
    if i % 3 == 0 and d[i // 3][0] + 1 < d[i][0]:
        d[i] = [d[i // 3][0] + 1, i // 3]
    if i % 2 == 0 and d[i // 2][0] + 1 < d[i][0]:
        d[i] = [d[i // 2][0] + 1, i // 2]

i = n
ret = []
while i > 0:
    ret.append(i)
    i = d[i][1]
print(d[n][0])
print(*ret)