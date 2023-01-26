import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())

if b <= a:
    print(a-b)
    for i in range(a, b-1,-1):
        print(i, end=" ")
    exit(0)

answer = 0

queue = deque()
visited = [[0, -1]]*100001

queue.append(a)
visited[a] = [a,0]


while queue:
    pos = queue.popleft()
    if pos == b:
        continue
    temp = visited[pos][1] + 1
    double = pos*2
    prev = pos-1
    after = pos+1
    
    if double <= 100000 and visited[double][1] < 0:
        queue.append(double)
        visited[double]= [pos, temp]
    if prev >= 0 and visited[prev][1] < 0:
        queue.append(prev)
        visited[prev]= [pos, temp]
    if after <= 100000 and visited[after][1] < 0:
        queue.append(after)
        visited[after]= [pos, temp]

print(visited[b][1])
path = deque()
path.appendleft(b)
while b != a:
    path.appendleft(visited[b][0])
    b = visited[b][0]

for i in path:
    print(i, end=" ")
