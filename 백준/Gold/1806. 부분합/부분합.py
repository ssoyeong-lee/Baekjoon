import sys
input = sys.stdin.readline

n, s = map(int, input().split())
li = list(map(int, input().split()))
li.append(0)

st = 0; en = 1
subSum = li[st]
ret = set()

while en < len(li):
    if subSum < s:
        subSum  += li[en]
        en += 1
    else:
        ret.add(en - st)
        subSum -= li[st]
        st += 1
if len(ret) == 0:
    print(0)
else:
    print(min(ret))