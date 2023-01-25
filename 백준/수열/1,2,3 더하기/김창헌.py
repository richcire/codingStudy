dp = [0] * 12
dp[0] = 1
dp[1] = 2
dp[2] = 4
for _ in range(int(input())):
  N = int(input())
  if N < 4:
    print(dp[N-1])
  else:
    for i in range(3, N):
      dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[N-1])