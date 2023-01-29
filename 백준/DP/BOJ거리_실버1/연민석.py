import sys

n = int(sys.stdin.readline())

roads = sys.stdin.readline().rstrip()

dp = [1000001]*(n)
dp[0] = 0

for i in range(1, n):
    if roads[i] == "B":
        for j in range(0,i):
            if roads[j] == "J":
                dp[i] = min(dp[i], dp[j] + (i-j)**2)
            
    elif roads[i] == "O":
        for j in range(0,i):
            if roads[j] == "B":
                dp[i] = min(dp[i], dp[j] + (i-j)**2)
    else:
        for j in range(0,i):
            if roads[j] == "O":
                dp[i] = min(dp[i], dp[j] + (i-j)**2)
    
if dp[-1] == 1000001:
    print(-1)
else:
    print(dp[-1])
