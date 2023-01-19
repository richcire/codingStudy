from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    arr[start] = 0
    while q:
        x = q.popleft()
        if x == K:
            return arr[x]
        for nx in (x*2, x+1, x-1):
            if 0 <= nx < 100001 and arr[nx] == -1:
                if nx == x*2:
                  arr[nx] = arr[x]
                  q.appendleft(nx)
                else:
                  arr[nx] = arr[x] + 1
                  q.append(nx)
        


N, K = map(int, input().split())
arr = [-1] * 100001

print(bfs(N))
