import sys
import heapq


INF = int(1e9)
input = sys.stdin.readline

def find(start):
  distance = [INF] * (n+1)
  q = []
  heapq.heappush(q,(0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in network[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
        
  return distance
  
for _ in range(int(input())):
  n,d,c = map(int,input().split())
  network = [[] for _ in range(n+1)]
  for _ in range(d):
    a,b,s = map(int, input().split())
    network[b].append((a,s))
  
  ans = find(c)
  max_dp = 0
  cnt = 0

  for i in ans:
    if i != INF: 
      if max_dp<i:
          max_dp = i
      cnt += 1
  print(cnt, max_dp)