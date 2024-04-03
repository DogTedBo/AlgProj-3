import heapq

# prim function
def prim(graph, start):
    min_spanning_tree = {}
    visited = set()
    edges = [(0, start, None)]
    heapq.heapify(edges)
    while edges:
        weight, node, prev_node = heapq.heappop(edges)
        if node not in visited:
            visited.add(node)
            if prev_node is not None:
                min_spanning_tree.setdefault(prev_node, []).append((node, weight))
                min_spanning_tree.setdefault(node, []).append((prev_node, weight))
            for neighbor, weight_info in graph[node].items():
                if neighbor not in visited:
                    edge_weight = weight_info['weight']
                    heapq.heappush(edges, (edge_weight, neighbor, node))
    return min_spanning_tree
