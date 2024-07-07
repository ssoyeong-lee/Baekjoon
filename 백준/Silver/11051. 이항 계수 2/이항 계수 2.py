n, k = map(int, input().split())
factorial = [1]
for i in range(1, n + 1):
  factorial.append(factorial[-1] * i)

# print(factorial)
print((factorial[n] // factorial[n - k] // factorial[k]) % 10007)