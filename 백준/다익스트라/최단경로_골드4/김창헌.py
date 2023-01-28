import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline
n,k = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
dis = [INF] * (n+1)

def find(s):
  q = []
  heapq.heappush(q, (0, s))
  dis[s] = 0
  while q:
    dist, now = heapq.heappop(q)
    if dis[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < dis[i[0]]:
        dis[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

for _ in range(k):
  s,e,v = map(int,input().split())
  graph[s].append((e,v))

find(start)
for i in range(1, n+1):
  if dis[i] == INF:
    print('INF')
  else:
    print(dis[i])