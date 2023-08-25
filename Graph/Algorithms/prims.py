import heapq

def prims(graph, root):
    mst, heap = [], [[0, root]]

    visited = set()

    while heap:
        cost, cur = heapq.heappop(heap)
        if cur in visited:
            continue

        visited.add(cur)
        mst.append([cur, cost])

        for vert, cost in graph[cur]:
            heapq.heappush(heap,[cost, vert])

        print(f"PICKED: {cur}\nHEAP: {heap}\nMST: {mst}\n")

    return mst


if __name__ == "__main__":
    graph = {"a":[["b",5], ["c", 14]],
             "b":[["a",5],["e",12], ["d",7]],
             "c":[["a",14],["f",8],["e",6]],
             "d":[["b",7], ["f",11],["e",4]],
             "e":[["c",6],["f",9],["b",12]],
             "f":[["d",11],["e",9],["c",8]]                       
            }
    mst = prims(graph,"a")
    print(f"MST: {mst}")