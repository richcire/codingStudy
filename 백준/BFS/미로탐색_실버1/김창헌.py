import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
maps = []
for _ in range(N):
  temp = list(input()) 
  temp.pop()
  for i in range(len(temp)):
    temp[i] = int(temp[i])
  maps.append(temp)

def bfs(y,x):
  q = deque()
  q.append((y,x))
  while q:
    y, x = q.popleft()
    for dx, dy in d:
      Y,X = y+dy, x+dx
      if 0<=Y<N and 0<=X<M and maps[Y][X] == 1:
        maps[Y][X] = maps[y][x] + 1
        q.append((Y,X))

d = [(0,1),(0,-1),(1,0),(-1,0)]
bfs(0,0)
print(maps[-1][-1])