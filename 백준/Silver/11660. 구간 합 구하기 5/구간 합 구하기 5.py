
import sys
sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
coord = [list(map(int, input().split())) for _ in range(m)]

sumTable = [[-1] * (n + 1) for _ in range(n + 1)]
for i in range(0, n + 1):
  sumTable[0][i] = sumTable[i][0] = 0


def calcSumTable(x, y):
  if sumTable[y - 1][x] == -1:
    calcSumTable(x, y - 1)
  if sumTable[y][x - 1] == -1:
    calcSumTable(x - 1, y)
  sumTable[y][x] = table[y - 1][x - 1] + sumTable[y - 1][x] + sumTable[y][x - 1] - sumTable[y - 1][x - 1]

ret = []
for y1, x1, y2, x2 in coord:
  if sumTable[y2][x2] == -1:
    calcSumTable(x2, y2)
  ret.append(sumTable[y2][x2] - sumTable[y2][x1 - 1] - sumTable[y1 - 1][x2] + sumTable[y1 - 1][x1 - 1])

print(*ret, sep='\n')