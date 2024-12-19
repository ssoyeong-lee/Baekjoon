import sys
input = sys.stdin.readline

def mul_matrix(A, B):
    C = []
    for a in range(n):
        tmp = []
        for b in range(k):
            emt = 0
            for c in range(m):
                emt += A[a][c] * B[c][b]
            tmp.append(emt)
        C.append(tmp)
    return C

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(m)]

C = mul_matrix(A, B)
for i in range(n):
    for j in range(k):
        print(C[i][j], end=' ')
    print()