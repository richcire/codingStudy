import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0

def bfs(i,j):
    bat[i][j] = 0
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0<=nx<N and 0<=ny<M and bat[nx][ny] == 1:
            bfs(nx, ny)

for _ in range(n):
    cnt = 0
    M, N, k = map(int, sys.stdin.readline().split())
    bat = [[0]*M for p in range(N)]
    for p in range(k):
        m, n = map(int, sys.stdin.readline().split())
        bat[n][m] = 1
    for i in range(N):
        for j in range(M):
            if bat[i][j] == 1:
                bfs(i,j)
                cnt+=1
    print(cnt)
