import sys

a = int(sys.stdin.readline())

map = [list(map(int, sys.stdin.readline().split())) for _ in range(a)]

graph = [[] for _ in range(a)]

answer = [[0]*a for _ in range(a)]

def dfs(i, j):
  visited.append(i)
  for gansun in graph[i]:
    if gansun == j:
      return 1
    if gansun in visited:
      continue
    if dfs(gansun, j):
      return 1
  return 0

for i in range(a):
  for j in range(a):
    if i == j:
      continue
    if map[i][j] == 1:
      graph[i].append(j)

for i in range(a):
  for j in range(a):
    # if i == j:
    #   answer[i][j] = 1
    #   continue
    visited = []
    answer[i][j] = dfs(i,j)

for i in range(a):
  for j in range(a):
    print(answer[i][j], end=" ")
  print()
