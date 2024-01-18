import sys
input = sys.stdin.readline

n = int(input())
nli = list(map(int, input().split()))
m = int(input())
mli = list(map(int, input().split()))

def binary_search(find):
    start = 0
    end = len(nli) - 1

    while start <= end:
        mid = (end + start) // 2
        if nli[mid] == find:
            return True
        elif nli[mid] < find:
            start = mid + 1
        else:
            end = mid - 1
    return False

nli.sort()
ret = []
for find in mli:
    if binary_search(find):
        ret.append(1)
    else:
        ret.append(0)
print(*ret, sep='\n')