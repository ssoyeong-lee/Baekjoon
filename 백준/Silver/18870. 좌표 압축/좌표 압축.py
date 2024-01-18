import sys
input = sys.stdin.readline

n = int(input())
lili = list(map(int, input().split()))

li = list(set(lili))
li.sort()

def bs(find):
    start = 0; end= len(li)
    while start <= end:
        mid = (start + end) // 2
        if li[mid] == find:
            return mid
        elif li[mid] > find:
            end = mid - 1
        else:
            start = mid + 1
    return 0

ret = []
for l in lili:
    ret.append(bs(l))
print(*ret)
