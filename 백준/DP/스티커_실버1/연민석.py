import sys

n = int(sys.stdin.readline())

for _ in range(n):
    dp = []
    k = int(sys.stdin.readline())
    dp.append(list(map(int, sys.stdin.readline().split())))
    dp.append(list(map(int, sys.stdin.readline().split())))

    if k == 1:
        print(max(dp[0][0], dp[1][0]))
        continue    

    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    for i in range(2,k):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][-1], dp[1][-1]))

