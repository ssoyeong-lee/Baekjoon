def delete(s):
    stack = []
    for i in s:
        if not stack or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()
    return ''.join(stack)

def solution(s):
    if len(s) % 2 == 1:
            return 0
    while s:
        r = delete(s)
        if len(s) == len(r):
            return 0
        s = r
    return 1