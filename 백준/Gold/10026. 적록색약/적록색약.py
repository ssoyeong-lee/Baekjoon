import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [input().rstrip() for _ in range(n)]

def bfs1(x, y):
    queue = deque([[x, y]])
    visited1[y][x] = True
    while queue:
        posX, posY = queue.popleft()
        for dx, dy in [[1, 0], [0, -1], [-1, 0], [0, 1]]:
            posX1 = posX + dx
            posY1 = posY + dy
            if 0 <= posX1 < n and 0 <= posY1 < n and visited1[posY1][posX1] == False:
                if board[posY][posX] == board[posY1][posX1]:
                    queue.append([posX1, posY1])
                    visited1[posY1][posX1] = True

def bfs2(x, y):
    queue = deque([[x, y]])
    visited2[y][x] = True
    while queue:
        posX, posY = queue.popleft()
        for dx, dy in [[1, 0], [0, -1], [-1, 0], [0, 1]]:
            posX1 = posX + dx
            posY1 = posY + dy
            if 0 <= posX1 < n and 0 <= posY1 < n and visited2[posY1][posX1] == False:
                if (board[posY][posX] == board[posY1][posX1]) or (board[posY][posX] != 'B' and board[posY1][posX1] != 'B'):
                    queue.append([posX1, posY1])
                    visited2[posY1][posX1] = True

visited1 = [[False] * n for _ in range(n)]; cnt1 = 0
visited2 = [[False] * n for _ in range(n)]; cnt2 = 0
for y in range(n):
    for x in range(n):
        if visited1[y][x] == False:
            bfs1(x, y)
            cnt1 += 1
        if visited2[y][x] == False:
            bfs2(x, y)
            cnt2 += 1
print(cnt1, cnt2)