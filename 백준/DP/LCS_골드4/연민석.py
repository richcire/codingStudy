import sys

one = sys.stdin.readline().rstrip()
two = sys.stdin.readline().rstrip()

one_len = len(one)
two_len = len(two)

dp = [0]*one_len

for i in range(two_len):
    temp = 0
    for j in range(one_len):
        if temp < dp[j]:
            temp = dp[j]
        elif two[i] == one[j]:
            dp[j] = temp + 1

print(max(dp))
    

