import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(map(int, input().split()))
li.append(1)

st = 0; en = 0
cnt = 0;  maxLen = 0
while st < len(li) and en < len(li):
    if li[en] % 2 == 0:
        en += 1
    else:
        if  cnt < k:
            cnt += 1
            en += 1
        else:
            maxLen = max(maxLen, en - st - cnt)
            if li[st] % 2 == 1:
                cnt -= 1
            st += 1
maxLen = max(maxLen, en - st - cnt)
print(maxLen)