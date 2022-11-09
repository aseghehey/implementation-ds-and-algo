from collections import defaultdict
class adjaceny_list:
    def __init__(self, n) -> None: 
        self.adjList = defaultdict(list)
        for i in range(n):
            self.adjList[i] = []
    
    def addEdge(self, u, v) -> None: 
        self.adjList[u].append(v)
    
    def removeEdge(self, u, v) -> None: 
        self.adjList[u].remove(v)

    def isAdjacent(self, u, v) -> bool: 
        return v in self.adjList[u]

    def getNeighbors(self, v) -> None: 
        print(f'neighbors: {self.adjList[v]}')
    
    def printGraph(self) -> None:
        print('Graph:')
        for v, e in self.adjList.items():
            print(f'{v} : {e}')

if __name__ == "__main__":
    graph = adjaceny_list(3)
    graph.addEdge(1,2)
    graph.addEdge(1,0)
    print(graph.isAdjacent(1,0))
    graph.getNeighbors(1)
    graph.removeEdge(1,0)
    graph.printGraph()
