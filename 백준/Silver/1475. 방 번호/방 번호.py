import math
number = input().rstrip()
ret = [0] * 10

for n in number:
  ret[int(n) - 1] += 1
tmp = math.ceil((ret[5] + ret[8]) / 2)
ret[5] = ret[8] = tmp
print(max(ret))