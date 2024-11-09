def get_cnt(n):
    cnt = 0
    while n > 0:
        cnt += n % 2
        n //= 2
    return cnt

def solution(n):
    cnt_n = get_cnt(n)
    nxt_n = n + 1
    while get_cnt(nxt_n) != cnt_n:
        nxt_n += 1
    return nxt_n
