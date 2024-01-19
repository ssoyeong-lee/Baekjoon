import sys
input = sys.stdin.readline

na, nb = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(); b.sort()

def bs(li, find):
    start = 0; end = len(li) - 1
    while start <= end:
        mid = (start + end) // 2
        if find < li[mid]:
            end = mid - 1
        elif find == li[mid]:
            return True
        else:
            start = mid + 1
    return False

ret = []
for i in a:
    if not bs(b, i):
        ret.append(i)

print(len(ret))
if len(ret) != 0:
    print(*ret)