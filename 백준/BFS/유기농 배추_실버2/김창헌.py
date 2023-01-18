import sys
from collections import deque

input = sys.stdin.readline
d = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(y, x):
  q = deque()
  q.append((y,x))
  maps[y][x] = 0
  while q:
    y,x = q.popleft()
    for dx, dy in d:
      Y, X = y+dy, x+dx
      if 0 <= Y < N and 0 <= X < M and maps[Y][X] == 1:
        maps[Y][X] = 0
        q.append((Y,X))
      
for _ in range(int(input())):
  M,N,K = map(int, input().split())
  maps = [[0]*M for _ in range(N)]
  for _ in range(K):
    x, y = map(int, input().split())
    maps[y][x] = 1
  ans = 0
  for i in range(N):
    for j in range(M):
      if maps[i][j] == 1:
        ans += 1
        bfs(i,j)
  print(ans)
