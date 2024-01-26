n = int(input())
net = [True] * (n + 1)

m = int(n ** 0.5)
for i in range(2, m + 1):
    if net[i]:
        for j in range(i * 2, n + 1, i):
            net[j] = False
li = [i for i in range(2, n + 1) if net[i]]
li.append(0)

st = 0; en = 1
tot = li[0]; cnt = 0

while en < len(li):
    if tot == n:
        cnt += 1
    if tot >= n:
        tot -= li[st]
        st += 1
    else:
        tot += li[en]
        en += 1
print(cnt)