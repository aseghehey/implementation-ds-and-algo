class adjacency_matrix:
    def __init__(self, n) -> None: # O(n^2)
        self.graph = [[0 for __ in range(n)] for _ in range(n)]
    
    def addEdge(self, u, v) -> None: # O(1)
        self.graph[u][v] = 1
    
    def removeEdge(self, u, v) -> None: # O(1)
        self.graph[u][v] = 0
    
    def isAdjacent(self, u, v) -> bool: # O(1)
        return True if self.graph[u][v] else False
    
    def getNeighbors(self, v) -> None: # O(n)
        for i in range(len(self.graph[v])):
            if self.graph[v][i]:
                print(f'neighbor with: {i}')
    
    def printGraph(self) -> None:
        print(self.graph)

if __name__ == '__main__':
    graph = adjacency_matrix(3)
    print(graph.isAdjacent(1,2))
    graph.addEdge(1,2)
    graph.addEdge(1,0)
    print(graph.isAdjacent(1,2))
    graph.getNeighbors(1)
    graph.printGraph()
    

