import sys

H, W = map(int, sys.stdin.readline().split())

walls = list(map(int, sys.stdin.readline().split()))

rain_sum = 0

world = [[1]*W for _ in range(H)]

for idx, wall in enumerate(walls):
    for i in range(wall):
        world[-(i+1)][idx] = 2

for i in world:
    temp = []
    temp_len = 0
    for idx, j in enumerate(i):
        if j == 2:
            temp.append(idx)
            temp_len+=1
    
    
    if temp_len >= 2:
        for k in range(temp_len-1):
            rain_sum += temp[k+1] - temp[k] - 1
        
print(rain_sum)



