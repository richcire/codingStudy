import sys
from collections import deque

m, n, k = map(int,sys.stdin.readline().split())

square = [[1]*n for _ in range(m)]

for _ in range(k):
  a,b,c,d = map(int, sys.stdin.readline().split())
  for i in range(b,d):
    for j in range(a,c):
      square[i][j] = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(i,j):
  result = 1
  queue = deque()
  queue.append((i,j))
  square[i][j] = 0
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<= nx < m and 0<= ny < n and square[nx][ny] == 1:
        result += 1
        square[nx][ny] = 0
        queue.append((nx, ny))
  return result

cnt = 0
answer = []

for i in range(m):
  for j in range(n):
    if square[i][j] == 1:
      cnt += 1
      answer.append(dfs(i,j))

answer.sort()
print(cnt)
for ans in answer:
  print(ans, end=" ")
