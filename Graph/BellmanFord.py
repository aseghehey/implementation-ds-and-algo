# given as [from, to, cost]
def bellman_Ford(graph, n, src, dst):
    cost = {f:float("inf") for f in range(n)}
    cost[src] = 0

    for i in range(n):
        tmp = cost.copy()
        for f,t,c in graph:
            if cost[f] == float("inf"):
                continue
            if c + cost[f] < tmp[t]:
                tmp[t] = c + cost[f]
        cost = tmp
    print(cost)
    return cost[dst]

arr = [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]]
print(bellman_Ford(arr, 5, 1, 4))