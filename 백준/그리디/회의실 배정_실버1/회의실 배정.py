import sys

input = sys.stdin.readline
N = int(input())
scheduel = []

for _ in range(N):
  s, e  = map(int, input().split())
  scheduel.append([s,e])

sch = sorted(scheduel, key=lambda x: (x[1], x[0]))

ans = 0
last = 0

for s, e in sch:
  if s >= last:
    ans += 1
    last = e

print(ans)