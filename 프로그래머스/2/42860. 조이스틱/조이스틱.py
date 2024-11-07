from math import ceil

def solution(name):
    ret = 0; idx = []; cur = prev = 100
    for i in range(len(name)):
        if name[i] == 'A':
            continue
        diff = ord(name[i]) - ord('A')
        ret += min(diff, 26 - diff)
        idx.append(i)
        if i <= len(name) - i:
            cur = i
        elif prev == 100:
            prev= cur
            cur = i

    if not idx:
        return 0
    go = idx[-1]
    if len(idx) == 1:
        back = len(name) - idx[0]
    elif idx[0] == 0:
        back = len(name) - idx[1]
    else:
        back = len(name) - idx[0] - 1
    cur = len(name) - cur
    return ret + min(go, back, prev * 2 + cur, prev + cur * 2)

            