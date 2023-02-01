import heapq  
import sys


def dijkstra(graph, start, n):
    result = {i: float('inf') for i in range(1,n+1)}
    result[start] = 0
    heap = []
    heapq.heappush(heap, [result[start], start])

    while heap:
        distance, destination = heapq.heappop(heap)

        if result[destination] < distance:
            continue
        
        for new_destination, new_distance in graph[destination].items():
            hubo = distance + new_distance
            if hubo < result[new_destination]:
                result[new_destination] = hubo
                heapq.heappush(heap, [hubo, new_destination])

    return result


N = int(sys.stdin.readline())

for _ in range(N):
    n, d, c = map(int, sys.stdin.readline().split())
    graph = {i:{} for i in range(1,n+1)}
    for i in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b][a] = s
    result = dijkstra(graph, c, n)
    cnt = 0
    last = 0
    for i in result.values():
        if i == float('inf'):
            continue
        cnt += 1
        if i > last:
            last = i
    print(cnt, last)





