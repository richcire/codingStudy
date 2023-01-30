import sys

n, m = map(int, sys.stdin.readline().split())

r, c, d = map(int, sys.stdin.readline().split())

map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

count = 0


while True:
    if map[r][c] == 0:
        map[r][c] = 2
        count += 1
    trapped = True
    for i in range(4):
        d -= 1
        if d < 0 :
            d = 3
        if d == 0:
            if r > 0 and map[r-1][c] == 0:
                r -= 1
                trapped = False
                break
        elif d == 1:
            if c < m-1 and map[r][c+1] == 0:
                c += 1
                trapped = False
                break
        elif d == 2:
            if r < n-1 and map[r+1][c] == 0:
                r += 1
                trapped = False
                break
        else:
            if c > 0 and map[r][c-1] == 0:
                c -= 1
                trapped = False
                break
    if trapped == True:
        if d == 0:
            if r < n-1 and map[r+1][c] != 1:
                r+=1
            else:
                break
        elif d == 1:
            if c > 0 and map[r][c-1] != 1:
                c -= 1
            else:
                break
        elif d == 2:
            if r > 0 and map[r-1][c] != 1:
                r -= 1
            else:
                break
        else:
            if c < m-1 and map[r][c+1] != 1:
                c += 1
            else:
                break

print(count)
        
