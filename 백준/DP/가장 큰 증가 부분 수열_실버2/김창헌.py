import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

dp = [1]*N
dp[0] = arr[0]

for i in range(N):
  for j in range(i):
    if arr[j] < arr[i]:
      dp[i] = max(arr[i]+dp[j], dp[i])
    else:
      dp[i] = max(arr[i], dp[i])
    
print(max(dp))