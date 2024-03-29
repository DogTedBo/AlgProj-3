#1 (1)BFS Can not find all connected components
def bfs(graph, start): 
    visited, queue = set(), [start] 
    p = []
    while queue: 
        vertex = queue.pop(0)
        if vertex not in visited: 
            visited.add(vertex)
            p.append(vertex)
            queue.extend(v for v in graph[vertex] if v not in visited) 
    return p

G = {'A': ['E', 'F', 'B'], 'B': ['A', 'F', 'C'], 'C': ['B', 'G', 'D'], 'D': ['C', 'G'], 'E': ['A', 'F', 'I'],
  'F': ['E', 'A', 'B'], 'G': ['D', 'C', 'J'], 'H': ['K', 'L'], 'I': ['E', 'F', 'J', 'M'], 'J': ['I', 'G'],
  'K': ['H', 'L', 'O'], 'L': ['H', 'K', 'P'], 'M': ['I', 'N'], 'N': ['M'], 'O': ['K'], 'P': ['L']}

print(bfs(G,'L'))
#1 (1)DFS Can not find all connected components

t=0
def dfs(graph, start, visited=None): 
    global t
    t += 1
    print('DSF called ', t, 'times.')
    if visited is None: 
        visited = set()
    visited.add(start)
    for key in set(graph[start]).difference(visited):  
       dfs(graph, key, visited)
    return visited 

G = {'A': ['E', 'F', 'B'], 'B': ['A', 'F', 'C'], 'C': ['B', 'G', 'D'], 'D': ['C', 'G'], 'E': ['A', 'F', 'I'],
  'F': ['E', 'A', 'B'], 'G': ['D', 'C', 'J'], 'H': ['K', 'L'], 'I': ['E', 'F', 'J', 'M'], 'J': ['I', 'G'],
  'K': ['H', 'L', 'O'], 'L': ['H', 'K', 'P'], 'M': ['I', 'N'], 'N': ['M'], 'O': ['K'], 'P': ['L']}

print(dfs(G,'A'))

#DFS 1 (2)
def dfs_paths(graph, start, goal): 
    stack = [(start, [start])]
    while stack:  
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal: 
               yield path + [next]
            else:
               stack.append((next, path + [next]))
  

G = {'A': ['E', 'F', 'B'], 'B': ['A', 'F', 'C'], 'C': ['B', 'G', 'D'], 'D': ['C', 'G'], 'E': ['A', 'F', 'I'],
  'F': ['E', 'A', 'B'], 'G': ['D', 'C', 'J'], 'H': ['K', 'L'], 'I': ['E', 'F', 'J', 'M'], 'J': ['I', 'G'],
  'K': ['H', 'L', 'O'], 'L': ['H', 'K', 'P'], 'M': ['I', 'N'], 'N': ['M'], 'O': ['K'], 'P': ['L']}

paths_generator = dfs_paths(G, 'A', 'J')

found_paths = list(paths_generator)
if found_paths:
    print("Paths found:")
    for path in found_paths:
        print(path)
else:
    print("No paths found.")

    #1 (2) BFS

    from collections import deque

def bfs_find_path(graph, start, goal):
    queue = deque([(start, [start])])  # Initialize queue with start node and its path
    visited = set([start])  # Keep track of visited nodes
    
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path  # Return the path if goal node is found
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))  # Enqueue neighbor node with updated path
    
    return None  # Return None if no path is found


start_node = 'A'
goal_node = 'G'

path = bfs_find_path(G, start_node, goal_node)
if path:
    print(f"Path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path found between {start_node} and {goal_node}")

