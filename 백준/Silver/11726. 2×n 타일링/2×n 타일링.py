n = int(input())

d = [0, 1, 2]
for i in range(3, n + 1):
  d.append((d[-2] + d[-1]) % 10007)
print(d[n])