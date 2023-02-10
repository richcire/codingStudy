from collections import deque

def bfs(x,y):
  q = deque()
  q.append((x,y))
  graph[x][y] = 0
  cnt = 1
  while q:
    x, y = q.popleft()
    for dx, dy in d:
      X,Y = x+dx, y+dy
      if 0<=X<n and 0<=Y<n and graph[X][Y] == 1:
        graph[X][Y] = 0
        q.append((X,Y))
        cnt += 1
  return cnt
        
n = int(input())
ans = []
d = [(1,0),(-1,0),(0,1),(0,-1)]
graph = [list(map(int, input())) for _ in range(n)]

for j in range(n):
  for i in range(n):
    if graph[i][j] == 1:
      ans.append(bfs(i,j))

print(len(ans))
ans.sort()
for i in ans:
  print(i)