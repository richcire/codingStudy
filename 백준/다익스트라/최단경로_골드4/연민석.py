import heapq  # 우선순위 큐 구현을 위함
import sys

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

graph = {i:{} for i in range(1,V+1)}

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if v in graph[u]:
        graph[u][v] = min(w, graph[u][v]) 
    else:   
        graph[u][v] = w


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


    
for i in dijkstra(graph, start).values():
    if i == float('inf'):
        print("INF")
    else: print(i)
