import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())

if b <= a:
    print(a-b)
    exit(0)

answer = 0

queue = deque()
visited = [-1]*100001

queue.append(a)
visited[a] = 0


while queue:
    pos = queue.popleft()
    if pos == b:
        break
    temp = visited[pos]
    double = pos*2
    prev = pos-1
    after = pos+1
    if double <= 100000 and visited[double] < 0:
        queue.append(double)
        visited[double]= temp
    if prev >= 0 and visited[prev] < 0:
        queue.append(prev)
        visited[prev]= temp + 1
    if after <= 100000 and visited[after] < 0:
        queue.append(after)
        visited[after]= temp + 1

print(visited[b])
