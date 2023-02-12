import sys
from collections import deque

n = int(sys.stdin.readline())

map = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

total = 0
result = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


for i in range(n):
    for j in range(n):
        if map[i][j] == "1":
            temp = 1
            total += 1
            map[i][j] = "0"
            queue = deque()
            queue.append((i,j))
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and map[nx][ny] == "1":
                        temp += 1
                        map[nx][ny] = "0"
                        queue.append((nx, ny))
            result.append(temp)

print(total)
result.sort()
for i in result:
    print(i, end=" ")

