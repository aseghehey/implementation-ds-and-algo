import heapq
from collections import defaultdict
arr = [[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]]

def clean(arr):
    adjlist = defaultdict(list)
    for src, to, w in arr:
        adjlist[src].append([to,w])
    return adjlist

def dijkstra(graph, src, dst, n):
    dist = {i: float('inf') for i in range(1, n + 1)}
    visited = set()

    pqueue = [[src, 0]]
    heapq.heapify(pqueue)

    while pqueue:
        cur, cst = heapq.heappop(pqueue)
        
        if cur in visited:
            continue

        visited.add(cur)
        dist[cur] = min(dist[cur], cst)

        for neighbor, cost in graph[cur]:
            if neighbor not in visited:
                heapq.heappush(pqueue, [neighbor, cost + cst])
    print(dist)
    return dist[dst]

print(dijkstra(clean(arr), 5, 4, 5))