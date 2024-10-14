from sys import stdin
input = stdin.readline

def solution(li, k):
  s = 0; e = k
  ret = [sum(li[s:e])]

  while e < len(li):
    ret.append(ret[-1] - li[s] + li[e])
    s += 1; e += 1
  return max(ret)

n, k = map(int, input().split())
li = list(map(int, input().split()))
print(solution(li, k))