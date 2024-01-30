from collections import defaultdict
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(map(int, input().split()))

cnt = defaultdict(int)
st = 0; en = 0
maxLen = 0
while en <= len(li):
    if en == len(li):
        maxLen = max(maxLen, en - st)
        break
    elif cnt[li[en]] == k:
        maxLen = max(maxLen, en - st)
        cnt[li[st]] -= 1
        st += 1
    else:
        cnt[li[en]] += 1
        en += 1

print(maxLen)