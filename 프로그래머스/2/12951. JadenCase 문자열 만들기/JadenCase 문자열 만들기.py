def solution(s):
    start, end = 0, 0
    ret = ''
    while end <= len(s):
        if end == len(s) or (s[start] == ' ' and s[end] != ' ') or (s[start] != ' ' and s[end] == ' '):
            ret += s[start].upper() + s[start + 1: end].lower()
            start = end
        end += 1

    return ret
        