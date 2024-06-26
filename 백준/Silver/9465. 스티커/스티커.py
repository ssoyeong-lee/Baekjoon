from sys import stdin

input = stdin.readline


def dp():
    # Input and preprocessing
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * n for _ in range(2)]
    dp[0][0] = scores[0][0]
    dp[1][0] = scores[1][0]
    if n > 1:
        dp[0][1] = dp[1][0] + scores[0][1]
        dp[1][1] = dp[0][0] + scores[1][1]

    # do dynamic programming
    for i in range(2, n):
        dp[0][i] = scores[0][i] + max(dp[0][i - 2], dp[1][i - 2], dp[1][i - 1])
        dp[1][i] = scores[1][i] + max(dp[0][i - 2], dp[1][i - 2], dp[0][i - 1])
    # return max val
    return max(dp[0][n - 1], dp[1][n - 1])


t = int(input())
ret = []
for _ in range(t):
    ret.append(dp())
print(*ret, sep="\n")
