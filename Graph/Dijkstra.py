import heapq
from collections import defaultdict
arr = [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]]

def clean(arr):
    adjlist = defaultdict(list)
    for src, to, w in arr:
        adjlist[src].append([to,w])
    return adjlist

def dijkstra(graph, src, dst, n):
    dist = {i: float('inf') for i in range(n)}
    visited = set()

    pqueue = [[src, 0]]
    heapq.heapify(pqueue)

    while pqueue:
        cur, cst = heapq.heappop(pqueue)
        visited.add(cur)
        dist[cur] = min(dist[cur], cst)
        for neighbor, cost in graph[cur]:
            if neighbor not in visited:
                heapq.heappush(pqueue, [neighbor, cost + cst])
    print(dist)
    return dist[dst]

print(dijkstra(clean(arr), 1, 4, 5))