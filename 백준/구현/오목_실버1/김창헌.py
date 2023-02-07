import sys


def bfs(x, y):
    target = graph[x][y]  # 바둑알의 색

    # 우/아래/대각선 우 아래/ 대각선 우 위 => 4가지 방향을 탐색
    for dx, dy in d:
        cnt = 1  # 바둑알 수
        nx = x + dx
        ny = y + dy

        # 반복문을 통해 오목이 되는지 확인
        while 0 <= nx < 19 and 0 <= ny < 19 and graph[nx][ny] == target:
            cnt += 1
            # 오목이라면
            if cnt == 5:
                # 육목 체크
                if 0 <= x - dx < 19 and 0 <= y - dy < 19 and graph[x - dx][
                        y - dy] == target:
                    break
                if 0 <= nx + dx < 19 and 0 <= ny + dy < 19 and graph[nx + dx][
                        ny + dy] == target:
                    break

                # 육목이 아니면 성공한 것으로
                # 바둑알의 색과 위치를 출력 후 종료
                print(target)
                print(x + 1, y + 1)
                exit(0)

            # 이전에 이동했던 방향으로 다시 이동
            nx += dx
            ny += dy


graph = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]

d = [(1, 0), (0, 1), (1, 1), (-1, 1)]
# 반복문을 통해 바둑알이 있는 위치를 탐색
for i in range(19):
    for j in range(19):
        if graph[i][j] != 0:
            bfs(i, j)

print(0)
