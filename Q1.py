#1 (1)BFS and DFS can find all connected components but not disconnected components
from collections import deque
from data3 import G
import networkx as nx
import matplotlib.pyplot as plt


def q1():
    
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



    print(bfs(G,'L'))
    #1 (1)DFS 

   
    # DFS
    def dfs(graph, start, visited=None): 
        global t
        t = 0
        t += 1
        print('DFS called ', t, 'times.')
        if visited is None: 
            visited = []
        visited.append(start)
        for key in set(graph[start]).difference(visited):  
            dfs(graph, key, visited)
        return visited 

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
  


    paths_generator = dfs_paths(G, 'A', 'G')

    found_paths = list(paths_generator)
    if found_paths:
        print("Paths found:")
        for path in found_paths:
            print(path)
    else:
        print("No paths found.")

    #1 (2) BFS

    

    def bfs_find_path(graph, start, goal):
        queue = deque([(start, [start])]) 
        visited = set([start]) 
    
        while queue:
            node, path = queue.popleft()
            if node == goal:
                return path
        
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor])) 
        return None 

    start_node = 'A'
    goal_node = 'G'

    path = bfs_find_path(G, start_node, goal_node)
    if path:
        print(f"Path from {start_node} to {goal_node}: {path}")
    else:
        print(f"No path found between {start_node} and {goal_node}")

    
    
    
    # Create a NetworkX graph
    G_nx = nx.Graph(G)

    # Plotting the graph
    plt.figure(figsize=(10, 8))

    # Draw the graph
    pos = nx.spring_layout(G_nx, seed=42)
    nx.draw(G_nx, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=12, font_weight='bold', edge_color='gray')

    plt.title('Graph without BFS and DFS Paths')
    plt.show()


