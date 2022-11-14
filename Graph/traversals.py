def dfs(graph, visited, vertex):
    if not vertex:
        return    
    print(vertex)
    visited.add(vertex)
    for n in graph[vertex]:
        if n not in visited:
            dfs(graph, visited, n)

def bfs(graph, vertex):
    visited = set()
    queue = [vertex]
    visited.add(vertex)
    while queue:
        v = queue.pop(0)
        print(v)
        for edges in graph[v]:
            if edges not in visited:
                visited.add(edges)
                queue.append(edges)
        
def main():
    graph = {0: [1,2], 1: [2,3], 2:[3], 3:[0]}
    visited = set()
    dfs(graph, visited, 1)
    print()
    bfs(graph, 1)


main()