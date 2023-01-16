import sys
from collections import deque

a, b = map(int,sys.stdin.readline().split())

maze = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(a)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


visited = []
queue = deque()

queue.append((0,0))

while queue:
  current = queue.popleft()
  for i in range(4):
    nextX = current[0] + dx[i]
    nextY = current[1] + dy[i]
    if (nextX, nextY) in visited:
      continue

    if 0<=nextX<a and 0<=nextY<b:
      if maze[nextX][nextY] > 1:
        maze[nextX][nextY] = min(maze[nextX][nextY], maze[current[0]][current[1]])
        queue.append((nextX, nextY))
        visited.append((nextX, nextY))
      elif maze[nextX][nextY] > 0:
        maze[nextX][nextY] = maze[current[0]][current[1]] + 1
        queue.append((nextX, nextY))
        visited.append((nextX, nextY))

print(maze[-1][-1])
