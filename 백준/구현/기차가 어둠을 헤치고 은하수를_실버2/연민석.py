import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

trains = [deque([0]*20) for _ in range(N)]

for _ in range(M):
    command = sys.stdin.readline()
    
    if command[0] == "1":
        _, i, x = map(int, command.split())
        trains[i-1][x-1] = 1
    elif command[0] == "2":
        _, i, x = map(int, command.split())
        trains[i-1][x-1] = 0
    elif command[0] == "3":
        _, i = map(int, command.split())
        trains[i-1].pop()
        trains[i-1].appendleft(0)
    else:
        _, i = map(int, command.split())
        trains[i-1].popleft()
        trains[i-1].append(0)

answer = 0
cache = []
for t in trains:
    if not t in cache:
        cache.append(t)
        answer+=1
print(answer)
