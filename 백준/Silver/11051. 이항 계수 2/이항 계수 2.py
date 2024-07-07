n, k = map(int, input().split())

tri = []
for i in range(n + 1):
  tmp = []
  for j in range(i + 1):
    if i == 0 or j == 0 or i == j:
      tmp.append(1)
    else:
      tmp.append((tri[-1][j - 1] + tri[-1][j]) % 10007)
  tri.append(tmp)
print(tri[n][k])