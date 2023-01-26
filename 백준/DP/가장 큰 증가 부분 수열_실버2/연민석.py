
import sys

a = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
dp = [0]*a


for i in range(a):
    for j in range(i):
        if lst[i] > lst[j] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += lst[i]

print(max(dp))
