import sys

N, M = map(int, sys.stdin.readline().split())

matrix = [[0]*(N+1)]
for _ in range(N):
    matrix.append([0] + list(map(int, sys.stdin.readline().split())))

    

for i in range(1,N+1):
    for j in range(1,N+1):
        matrix[i][j] = matrix[i][j] + matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(matrix[x2][y2] - matrix[x2][y1-1] - matrix[x1-1][y2] + matrix[x1-1][y1-1])

