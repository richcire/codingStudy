import sys

n = int(sys.stdin.readline())

podoju = []

for _ in range(n):
    podoju.append(int(sys.stdin.readline()))

if n == 1:
    print(podoju[0])
    exit(0)
if n == 2:
    print(podoju[0] + podoju[1])
    exit(0)

dp = []
dp.append(podoju[0])
dp.append(podoju[0] + podoju[1])
dp.append(max(dp[1], podoju[1]+podoju[2], podoju[0]+podoju[2]))
for i in range(3,n):
    dp.append(max(dp[i-3] + podoju[i-1] + podoju[i], dp[i-2]+podoju[i], dp[i-1]))

print(dp[-1])
