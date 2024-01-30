import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
li = [int(input()) for _ in range(n)]
for i in range(k):
    li.append(li[i])

ret = 0
st = 0
while st + k < len(li):
    checker = set(li[st: st + k])
    checker.add(c)
    ret = max(ret, len(checker))
    st += 1

print(ret)