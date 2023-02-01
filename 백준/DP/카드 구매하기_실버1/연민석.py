import sys

n = int(sys.stdin.readline())

cost = [0] + list(map(int, sys.stdin.readline().split()))

dp=[0]*(n+1)

for i in range(1,n+1):
    for j in range(1,i):
        dp[i] = max(dp[i], (i//j)*dp[j]+dp[i%j])
    dp[i] = max(dp[i], cost[i])

print(dp[-1])
