import networkx as nx
import matplotlib.pyplot as plt
from data3 import edges
from dijkstra import dijkstra
from prim import prim

def visualize_graph():
    # Create the graph from the edges data
    graph = nx.Graph()
    graph.add_weighted_edges_from(edges)

    # Define the starting node
    start_node = 'A'

    # Calculate and print the shortest paths from the starting node
    print("Shortest paths from", start_node + ":")
    shortest_paths = dijkstra(graph, start_node)
    for node, distance in shortest_paths.items():
        print(f"To {node}: {distance}")

    # Get the edges of the shortest paths
    shortest_path_edges = [(start_node, node) for node in shortest_paths if node != start_node]

    # Calculate and print the minimum spanning tree
    print("\nMinimum spanning tree:")
    min_spanning_tree = prim(graph, start_node)
    for node, neighbors in min_spanning_tree.items():
        for neighbor, weight in neighbors:
            print(f"{node} - {neighbor}: {weight}")

    # Visualize the graph, shortest paths, and minimum spanning tree
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(graph, seed=42)  # Adjust the layout for better visualization

    # Draw the graph nodes and labels
    nx.draw_networkx_nodes(graph, pos, node_color='skyblue', node_size=700)
    nx.draw_networkx_labels(graph, pos, font_size=12, font_color='black', font_weight='bold')

    # Draw the graph edges with different styles for shortest paths and minimum spanning tree
    nx.draw_networkx_edges(graph, pos, edgelist=graph.edges(), width=1, alpha=0.5, edge_color='gray')
    nx.draw_networkx_edges(graph, pos, edgelist=shortest_path_edges, width=2, alpha=0.8, edge_color='red', style='dashed')
    min_spanning_tree_edges = [(node, neighbor) for node, neighbors in min_spanning_tree.items() for neighbor, _ in neighbors]
    nx.draw_networkx_edges(graph, pos, edgelist=min_spanning_tree_edges, width=2, alpha=0.8, edge_color='green')

    # Add edge labels
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    plt.title("Graph with Shortest Paths (Red, Dashed) and Minimum Spanning Tree (Green)")
    plt.axis('off')  # Disable axis
    plt.show()

