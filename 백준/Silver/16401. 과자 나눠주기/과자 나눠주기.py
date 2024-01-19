import sys
input = sys.stdin.readline

m, n = map(int, input().split())
li = list(map(int, input().split()))

def getCnt(length):
    cnt = 0
    for i in li:
        cnt += i // length
    return cnt

def bs():
    global m
    
    start = 0; end = max(li)
    while start < end:
        mid = (start + end + 1) // 2
        cnt = getCnt(mid)
        if cnt < m:
            end = mid - 1
        else:
            start = mid
    return start

print(bs())