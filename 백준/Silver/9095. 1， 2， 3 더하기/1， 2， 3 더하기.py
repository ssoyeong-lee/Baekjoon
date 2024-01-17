n = int(input())

dp = [0, 1, 2, 4]
for _ in range(n):
    t = int(input()) 
    for i in range(len(dp), t + 1): 
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
    print(dp[t])