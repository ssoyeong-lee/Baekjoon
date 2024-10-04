from sys import stdin
from collections import defaultdict
from math import sqrt
input = stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b, rank):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a == root_b:
        return
    if rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    else:
        parent[root_b] = root_a
        if rank[root_a] == rank[root_b]:
            rank[root_a] += 1

def get_path_dict(path):
    ret = defaultdict(set)
    for a, b in path:
        if a < b:
            ret[a - 1].add(b - 1)
        else:
            ret[b - 1].add(a - 1)
    return ret

def get_dist(pos, a, b):
    x1, y1 = pos[a]
    x2, y2 = pos[b]
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

def solution(pos, path):
    ret = 0; cnt = len(path)
    parent = [i for i in range(len(pos))]
    rank = [0] * len(pos)

    path = get_path_dict(path)
    
    dist = []
    for a in range(len(pos)):
        for b in range(a + 1, len(pos)):
            if b in path[a]:
                union(parent, a, b, rank)
            else:
                dist.append((get_dist(pos, a, b), a, b))
    dist.sort()

    for d, a, b in dist:
        if find(parent, a) == find(parent, b):
            continue
        union(parent, a, b, rank)
        ret += d
        cnt += 1
        if cnt == len(pos):
            break
    return ret


n, m = map(int, input().split())
pos = [list(map(int, input().split())) for _ in range(n)]
path = [list(map(int, input().split())) for _ in range(m)]
print(f'{round(solution(pos, path), 2):.2f}')