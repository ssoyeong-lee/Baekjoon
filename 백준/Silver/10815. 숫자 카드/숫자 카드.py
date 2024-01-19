import sys
input = sys.stdin.readline

n = int(input())
nli = list(map(int, input().split()))
m = int(input())
mli = list(map(int, input().split()))

nli.sort()

def bs(find):
    start = 0; end = len(nli) - 1
    while start <= end:
        mid = (start + end) // 2
        if nli[mid] == find:
            return 1
        elif nli[mid] > find:
            end = mid - 1
        else:
            start = mid + 1
    return 0

ret = []
for i in mli:
    ret.append(bs(i))
print(*ret)