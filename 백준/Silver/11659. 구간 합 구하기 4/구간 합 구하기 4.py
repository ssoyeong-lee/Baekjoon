import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
li2 = [0]
for i in li:
  li2.append(li2[-1] + i)
ret = []
for _ in range(m):
  i, j = map(int, input().split())
  ret.append(li2[j] - li2[i - 1])
print(*ret, sep='\n')