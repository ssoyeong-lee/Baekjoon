def solution(s, skip, index):
    alpha = []
    for i in range(ord('a'), ord('z') + 1):
        if chr(i) not in skip:
            alpha.append(chr(i))
    print(alpha)
    a = ord('a')
    ret = []
    for tmp in s:
        pos = 0
        while alpha[pos] != tmp:
            pos += 1
        ret.append(alpha[(pos + index) % len(alpha)])
    return ''.join(ret)
    
    