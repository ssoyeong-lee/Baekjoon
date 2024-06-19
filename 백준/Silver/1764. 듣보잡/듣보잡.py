import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set([input().rstrip() for _ in range(n)])
b = set([input().rstrip() for _ in range(m)])
ret = list(a.intersection(b))
ret.sort()
print(len(ret))
print(*ret, sep='\n')