import heapq  # 우선순위 큐 구현을 위함
import sys

V, E = map(int, sys.stdin.readline().split())


graph = {i:{} for i in range(1,V+1)}

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u][v] = w
    graph[v][u] = w

v1, v2 = map(int, sys.stdin.readline().split())


def dijkstra(graph, start):
    result = {i: float('inf') for i in range(1,V+1)}
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

one_start = dijkstra(graph, 1)
v1_start = dijkstra(graph, v1)
v2_start = dijkstra(graph, v2)

v1_v2 = one_start[v1] + v1_start[v2] +v2_start[V]
v2_v1 = one_start[v2]+ v2_start[v1] + v1_start[V]

if v1_v2 == float('inf') and v2_v1 == float('inf'):
    print(-1)
else:
    print(min(v1_v2 , v2_v1))
