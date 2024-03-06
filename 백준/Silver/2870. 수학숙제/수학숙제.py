alpha = set('abcdefghijklmnopqrstuvwxyz')

def solve(line):
  li = []
  tag = True
  for l in line:
    if l not in alpha:
      if tag:
        li.append('')
        tag = False
      li[-1] += l
    else:
      tag = True
  return list(map(int, li))

n = int(input())
ret = []
for _ in range(n):
  ret += solve(input())
ret.sort()
print(*ret, sep='\n')