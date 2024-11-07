def solution(s):
    DIFF = ord('a') - ord('A')
    
    ret = ''
    start = 0
    for i in range(len(s)):
        idx = i - start
        if s[i] == ' ':
            ret += ' '
            start = i + 1
        elif idx % 2 == 0 and 'a' <= s[i] <= 'z':
            ret += chr(ord(s[i]) - DIFF)
        elif idx % 2 == 1 and 'A' <= s[i] <= 'Z':
            ret += chr(ord(s[i]) + DIFF)
        else:
            ret += s[i]
    return ret