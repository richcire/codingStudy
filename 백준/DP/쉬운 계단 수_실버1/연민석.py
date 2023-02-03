import sys

n = int(sys.stdin.readline())

dp = {i:1 for i in range(1,10)}
dp[0] = 0

if n == 1:
    print(9)
    exit(0)

for i in range(2,n+1):
    prev = dp.copy()
    for j in range(1,9):
        dp[j] = (prev[j-1] + prev[j+1])%1000000000 
    dp[0] = prev[1]
    dp[9] = prev[8]

print(sum(dp.values()) % 1000000000)
