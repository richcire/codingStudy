import sys

n, start, maximum = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))

dp = [[0]*(maximum+1) for _ in range(n+1)]


dp[0][start] = 1

for i in range(n):
    for idx, j in enumerate(dp[i]):
        if j == 1:
            if idx + lst[i] <= maximum:
                dp[i+1][idx + lst[i]] = 1
            if idx-lst[i] >= 0:
                dp[i+1][idx - lst[i]] = 1

for i in range(maximum, -1, -1):
    if dp[-1][i] == 1:
        print(i)
        exit(0)

print(-1)
