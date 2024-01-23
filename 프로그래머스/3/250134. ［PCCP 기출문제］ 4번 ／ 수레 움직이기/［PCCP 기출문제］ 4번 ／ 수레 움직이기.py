from collections import deque

delta = [[1, 0], [0, -1], [-1, 0], [0, 1]]

n = m = 0
ret = set()
visitedR = []
visitedB = []

def getCandidate(maze, x, y, dst, visited):
    if maze[y][x] == dst:
        return [[x, y]]
    res = []
    for dx, dy in delta:
        x1, y1 = x + dx, y + dy
        if 0 <= x1 < m and 0 <= y1 < n and not visited[y1][x1]:
            res.append([x1, y1])
    return res

def dfs(maze, rx, ry, bx, by, cnt):
    global ret, m, n, visitedR, visitedB
    if maze[ry][rx] == 3 and maze[by][bx] == 4:
        ret.add(cnt)
        return

    nextR = getCandidate(maze, rx, ry, 3, visitedR)
    nextB = getCandidate(maze, bx, by, 4, visitedB)
    
    for rx1, ry1 in nextR:
        for bx1, by1 in nextB:

            if not (0 <= rx1 < m and 0 <= ry1 < n and 0 <= bx1 < m and 0 <= by1 < n):
                continue
            if maze[ry1][rx1] == 5 or maze[by1][bx1] == 5:
                continue
            if rx1 == bx1 and ry1 == by1:
                continue
            if rx1 == bx and ry1 == by and bx1 == rx and by1 == ry:
                continue
            
            visitedR[ry1][rx1] = True
            visitedB[by1][bx1] = True
            dfs(maze, rx1, ry1, bx1, by1, cnt + 1)
            visitedR[ry1][rx1] = False
            visitedB[by1][bx1] = False       
    
                    
def solution(maze):
    global m, n, ret, visitedR, visitedB
    n = len(maze)
    m = len(maze[0])

    visitedR = [[False] * m for _ in range(n)]
    visitedB = [[False] * m for _ in range(n)]

    tmp = [0, 0, 0, 0, 0]
    for y in range(n):
        for x in range(m):
            if maze[y][x] == 1:
                tmp[0], tmp[1] = x, y
                visitedR[y][x] = True
            elif maze[y][x] == 2:
                tmp[2], tmp[3] = x, y
                visitedB[y][x] = True
    
    dfs(maze, *tmp)
    if len(ret) == 0:
        return 0
    return min(ret)
                
                
    
                