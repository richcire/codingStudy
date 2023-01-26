import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())

if b <= a:
    print(a-b)
    print(1)
    exit(0)

answer = 0

queue = deque()
visited = [b-a]*100001

queue.append(a)
visited[a] = 0


while queue:
    pos = queue.popleft()
    if pos == b:
        answer += 1
        continue
    temp = visited[pos] + 1
    double = pos*2
    prev = pos-1
    after = pos+1
    
    if double <= 100000 and visited[double] >= temp:
        queue.append(double)
        visited[double]= temp
    if prev >= 0 and visited[prev] >= temp:
        queue.append(prev)
        visited[prev]= temp
    if after <= 100000 and visited[after] >= temp:
        queue.append(after)
        visited[after]= temp

print(visited[b])
print(answer)
