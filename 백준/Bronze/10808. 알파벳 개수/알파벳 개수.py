from collections import Counter

ret = [0] * 26
counter = Counter(input().rstrip())
standard = ord('a')
for i in range(26):
  ret[i] = counter[chr(i + standard)]
print(*ret)