import sys

input = sys.stdin.readline
n, m = map(int,input().split())
puzzle = [input().rstrip() for _ in range(n)]
ans = []

for i in range(m):
  sig = ''
  for j in range(n):
    sig+=puzzle[j][i]
    temp = sig.split('#')
  for x in temp:
      if len(x) > 1:
        ans.append(x)

for i in puzzle:
    temp = i.split('#')
    for j in temp:
      if len(j) > 1:
        ans.append(j)

ans.sort()
print(ans[0])