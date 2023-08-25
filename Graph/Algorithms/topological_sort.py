# used in directed graphs, linear ordering where an edge (v, u) would have vertex (v) come before (u)

directed_graph = {
		1: [3],
		2: [3],
		3: [],
		4: [1, 2]
		}

stack = []
visited = set()
def topological_sort(node):
	visited.add(node)
	for neighbor in directed_graph[node]:
		if neighbor not in visited:
			topological_sort(neighbor)
	stack.append(node)

for k in directed_graph.keys():
	if k not in visited:
		topological_sort(k)

print(stack[::-1])
