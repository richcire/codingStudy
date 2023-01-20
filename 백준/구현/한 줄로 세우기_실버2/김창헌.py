import sys

input = sys.stdin.readline
n = int(input())
people = list(map(int, input().split()))
ans = [0] * n

for per in range(1, n+1):
    target = people[per-1]
    cnt = 0
    for i in range(n):
      if cnt == target and ans[i] == 0:
          ans[i] = per
          break
      elif ans[i] == 0:
          cnt += 1

print(*ans)