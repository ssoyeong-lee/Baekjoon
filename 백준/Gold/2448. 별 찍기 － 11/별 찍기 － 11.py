import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())

k = 0
tmp = n // 3
while tmp != 1:
    tmp //= 2
    k += 1

m = 5
for _ in range(k):
    m = 2 * m + 1

star = [[' '] * m for _ in range(n)]

def draw_star(x, y, w, h):
    if h == 3:
        star[y][x + 2] = '*'
        star[y + 1][x + 1] = '*'
        star[y + 1][x + 3] = '*'
        star[y + 2][x] = '*'
        star[y + 2][x + 1] = '*'
        star[y + 2][x + 2] = '*'
        star[y + 2][x + 3] = '*'
        star[y + 2][x + 4] = '*'
        return
    draw_star(x + w // 4 + 1, y, (w - 1) // 2, h // 2)
    draw_star(x, y + h // 2, (w - 1) // 2, h // 2)
    draw_star(x + w // 2 + 1, y + h // 2, (w - 1) // 2, h // 2)

draw_star(0, 0, m, n)
for s in star:
    print("".join(s))