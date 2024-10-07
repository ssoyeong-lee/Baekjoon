import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
ret = []
# def mid_idx_find(s, e, root):
#   for i in range(s, e):
#     if mid[i] == root:
#       return i
#   return -1

def solution(mid_s, mid_e, post_s, post_e):
  if mid_s >= mid_e:
    return
  root = post[post_e - 1]
  ret.append(root)
  mid_root_idx = mid_idx[root]
  
  left_mid_s = mid_s
  left_mid_e = mid_root_idx
  right_mid_s = mid_root_idx + 1
  right_mid_e = mid_e

  left_post_s = post_s
  left_post_e = post_s + (left_mid_e - left_mid_s)
  right_post_s = left_post_e
  right_post_e = post_e - 1

  solution(left_mid_s, left_mid_e, left_post_s, left_post_e)
  solution(right_mid_s, right_mid_e, right_post_s, right_post_e)


n = int(input())
mid = list(map(int, input().split()))
post = list(map(int, input().split()))
mid_idx = {mid[i]: i for i in range(n)}
solution(0, n, 0, n)
print(*ret)