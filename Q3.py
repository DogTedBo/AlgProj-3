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


    # Visualization
    pos = nx.spring_layout(graph, scale=3, seed=42)  # Position nodes using Fruchterman-Reingold force-directed algorithm with larger scale
    labels = nx.get_edge_attributes(graph, 'weight')  # Get edge weights as labels

    # Draw graph
    nx.draw_networkx_nodes(graph, pos, node_color='skyblue', node_size=700)
    nx.draw_networkx_edges(graph, pos, edge_color='gray', width=1.5)
    nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=10)

    # Highlight shortest path edges with reduced transparency
    nx.draw_networkx_edges(graph, pos, edgelist=shortest_path_edges, edge_color='green', alpha=0.5, width=2.0)

    plt.title('Graph Visualization')
    plt.axis('off')  # Turn off axis
    plt.show()
