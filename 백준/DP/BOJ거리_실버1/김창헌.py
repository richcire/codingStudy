N = int(input())
road = list(input())
dp = [float('inf')] * N
dp[0] = 0
for i in range(1, N):
  for j in range(i):
    sig = 0
    if road[i] == 'B' and road[j] == 'J':
      dp[i] = min(dp[i], dp[j]+(i-j)**2)
    if road[i] == 'O' and road[j] == 'B':
      dp[i] = min(dp[i], dp[j]+(i-j)**2)
    if road[i] == 'J' and road[j] == 'O':
      dp[i] = min(dp[i], dp[j]+(i-j)**2)

if dp[-1] != float('inf'):
  print(dp[-1])
else:
  print(-1)