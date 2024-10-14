from sys import stdin
input = stdin.readline

def solution(board, k):
  n, m = len(board), len(board[0])
  cnt_black = [[0] * (m + 1) for _ in range(n + 1)]
  cnt_white = [[0] * (m + 1) for _ in range(n + 1)]
  ret = k * k
  for y in range(1, n + 1):
    for x in range(1, m + 1):
      cnt_black[y][x] = cnt_black[y - 1][x] + cnt_black[y][x - 1] - cnt_black[y - 1][x - 1]
      cnt_white[y][x] = cnt_white[y - 1][x] + cnt_white[y][x - 1] - cnt_white[y - 1][x - 1]
      is_odd = True if (x + y) % 2 == 1 else False
      if (not is_odd and board[y - 1][x - 1] == 'W') or (is_odd and board[y - 1][x - 1] == 'B'):
        cnt_black[y][x] += 1
      elif (is_odd and board[y - 1][x - 1] == 'W') or (not is_odd and board[y - 1][x - 1] == 'B'):
        cnt_white[y][x] += 1
      if x >= k and y >= k:
        ret = min(ret, cnt_black[y][x] - cnt_black[y - k][x] - cnt_black[y][x - k] + cnt_black[y - k][x - k], \
                  cnt_white[y][x] - cnt_white[y - k][x] - cnt_white[y][x - k] + cnt_white[y - k][x - k])
  return ret

n, m, k = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
print(solution(board, k))