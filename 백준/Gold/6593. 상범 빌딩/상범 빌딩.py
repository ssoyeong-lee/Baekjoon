from collections import deque
from sys import stdin
input = stdin.readline

# solution: bfs
def solution(arr):
    l, r, c = len(arr), len(arr[0]), len(arr[0][0])
    dist = [[[-1] * c for _ in range(r)] for __ in range(l)]
    
    dq = deque()
    for z in range(l):
        for y in range(r):
            for x in range(c):
                if arr[z][y][x] == 'S':
                    dq.append((x, y, z))
                    dist[z][y][x] = 0
                    break
    
    while dq:
        x1, y1, z1 = dq.popleft()
        if arr[z1][y1][x1] == 'E':
            return dist[z1][y1][x1]
        for dx, dy, dz in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)):
            x2, y2, z2 = x1 + dx, y1 + dy, z1 + dz
            if 0 <= x2 < c and 0 <= y2 < r and 0 <= z2 < l:
                if dist[z2][y2][x2] == -1 and arr[z2][y2][x2] != '#':
                    dist[z2][y2][x2] = dist[z1][y1][x1] + 1
                    dq.append((x2, y2, z2))
    return -1

# input
ret = []
while True:
    l, r, c = map(int, input().split())
    if l == r == c == 0:
        break

    arr = []
    for z in range(l):
        arr.append([input().rstrip() for _ in range(r)])
        input()
    ret.append(solution(arr))

for time in ret:
    print(f'Escaped in {time} minute(s).' if time != -1 else 'Trapped!')