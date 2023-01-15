import sys

n = int(sys.stdin.readline())

L = list(map(int, sys.stdin.readline().split()))
J = list(map(int, sys.stdin.readline().split()))

dp = [0]*100

for i in range(n):
  for j in range(99, L[i]-1, -1):
    dp[j] = max(dp[j], dp[j - L[i]] + J[i])

print(dp[99])

#처음엔 조합 패키지 임포트해서 브루트포스로 품
