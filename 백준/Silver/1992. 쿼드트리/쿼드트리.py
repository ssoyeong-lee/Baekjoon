import sys
input = sys.stdin.readline

n = int(input())
li = [list(input().rstrip()) for _ in range(n)]

def quad_tree(r, c, n):
    global li
    if n == 1:
        print(li[r][c], end='')
        return
    val = li[r][c]; tag = False
    for y in range(r, r + n):
        for x in range(c, c + n):
            if li[y][x] != val:
                tag = True
                break
        if tag:
            break
    if tag:
        print('(', end='')
        quad_tree(r, c, n // 2)
        quad_tree(r, c + n // 2, n // 2)
        quad_tree(r + n // 2, c, n // 2)
        quad_tree(r + n // 2, c + n // 2, n // 2)
        print(')', end='')
    else:
        print(val, end='')

quad_tree(0, 0, n)
print()