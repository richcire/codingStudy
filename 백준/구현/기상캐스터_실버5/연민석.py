import sys

a, b = map(int, sys.stdin.readline().split())

map = [sys.stdin.readline().rstrip() for _ in range(a)]

answer = [[0]*b for _ in range(a)]

for i in range(a):
  for j in range(b):
    if map[i][j] == "c":
      continue
    if j == 0:
      answer[i][j] = -1
      continue
    if answer[i][j-1] == -1:
      answer[i][j] = -1
      continue
    answer[i][j] = answer[i][j-1] + 1

for i in range(a):
  for j in range(b):
    print(answer[i][j], end=" ")
  print()
