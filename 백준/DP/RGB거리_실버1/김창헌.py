import sys

input = sys.stdin.readline
n = int(input())
d = [[0,0,0] for _ in range(n)]
pay = [list(map(int, input().split())) for _ in range(n)]
d[0] = pay[0]

for i in range(1, n):
  d[i][0] = min(d[i-1][1]+pay[i][0], d[i-1][2]+pay[i][0])
  d[i][1] = min(d[i-1][0]+pay[i][1], d[i-1][2]+pay[i][1])
  d[i][2] = min(d[i-1][0]+pay[i][2], d[i-1][1]+pay[i][2])

print(min(d[-1]))

  