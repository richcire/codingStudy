import sys

input = sys.stdin.readline
dp = [0]*90
dp[0] = 1
dp[1] = 1
N = int(input())
for i in range(2, N):
  dp[i] = dp[i-2] + dp[i-1]

print(dp[N-1])