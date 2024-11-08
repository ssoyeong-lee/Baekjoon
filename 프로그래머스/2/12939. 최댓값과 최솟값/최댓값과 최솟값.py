def solution(s):
    s = list(map(int, s.split()))
    s.sort()
    return f'{s[0]} {s[-1]}'