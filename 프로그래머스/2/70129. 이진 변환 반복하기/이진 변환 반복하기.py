from collections import Counter

def to_binary(n):
    ret = Counter()
    while n > 0:
        ret[str(n % 2)] += 1
        n //= 2
    return ret
    
def solution(s):
    ret = [0, 0]

    cnt = Counter(list(s))
    while not (cnt['1'] == 1 and cnt['0'] == 0):
        ret[0] += 1
        ret[1] += cnt['0']
        cnt = to_binary(cnt['1'])
        
    return ret
    