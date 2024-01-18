import sys
input = sys.stdin.readline

n = int(input())
nli = list(map(int, input().split()))
m = int(input())
mli = list(map(int, input().split()))
nli.sort()

def bs_start(find):
    start = 0; end = len(nli); mid = 0
    while start < end:
        mid = (start + end) // 2
        if nli[mid] >= find:
            end = mid
        else:
            start = mid + 1
    return start

def bs_end(find):
    start = 0; end = len(nli); mid = 0
    while start < end:
        mid = (start + end) // 2
        if nli[mid] > find:
            end = mid
        else:
            start = mid + 1
    return start

ret = []
for t in mli:
    ret.append(bs_end(t) - bs_start(t))
print(*ret)