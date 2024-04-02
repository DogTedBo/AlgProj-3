import networkx as nx
import matplotlib.pyplot as plt


# Define the array of edges for the graph
edges = [
    ("A", "B", 22), ("A", "C", 9), ("A", "D", 12),
    ("B", "C", 35), ("B", "H", 34), ("H", "I", 19),
    ("I", "D", 30), ("D", "C", 4), ("D", "E", 33),
    ("B", "F", 36), ("H", "F", 24), ("F", "G", 39),
    ("F", "E", 18), ("C","E", 65), ("C", "F", 42),
    ("G", "E", 23), ("G", "H", 25), ("G", "I", 21)
]

G = {'A': ['E', 'F', 'B'], 'B': ['A', 'F', 'C'], 'C': ['B', 'G', 'D'], 'D': ['C', 'G'], 'E': ['A', 'F', 'I'],
  'F': ['E', 'A', 'B'], 'G': ['D', 'C', 'J'], 'H': ['K', 'L'], 'I': ['E', 'F', 'J', 'M'], 'J': ['I', 'G'],
  'K': ['H', 'L', 'O'], 'L': ['H', 'K', 'P'], 'M': ['I', 'N'], 'N': ['M'], 'O': ['K'], 'P': ['L']}

edges1 = [
    (1, 2), (1, 3), (2, 4), (3, 4), (4, 3), (4, 5), (5, 6), (5, 11),
    (6, 7), (7, 8), (8, 9), (9, 6), (9, 10), (11, 12), (12, 10), (10, 5)
]


def draw_weighted_graph(edges):

    # Create a graph object
    G_weighted = nx.Graph()

    # Add edges with weights to the graph
    for edge in edges:
        G_weighted.add_edge(edge[0], edge[1], weight=edge[2])

    # Draw the graph
    pos = nx.spring_layout(G_weighted)
    nx.draw(G_weighted, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=10, font_weight="bold")
    labels = nx.get_edge_attributes(G_weighted, 'weight')
    nx.draw_networkx_edge_labels(G_weighted, pos, edge_labels=labels)
    plt.title("Weighted Graph")
    plt.show()





def draw_simple_graph(G):
   

    # Create a graph object
    G_simple = nx.Graph(G)

    # Draw the graph
    plt.figure(figsize=(10, 8))
    pos_simple = nx.spring_layout(G_simple)
    nx.draw(G_simple, pos_simple, with_labels=True, node_size=1500, node_color="lightgreen", font_size=10, font_weight="bold")
    plt.title("Simple Graph (without edge weights)")
    plt.show()



# Create a graph object
def draw_graph_with_edges(edges1):

    # Create a graph object
    G_edges = nx.Graph()

    # Add edges to the graph
    G_edges.add_edges_from(edges1)

    # Draw the graph
    plt.figure(figsize=(10, 8))
    pos_edges = nx.spring_layout(G_edges)
    nx.draw(G_edges, pos_edges, with_labels=True, node_size=1500, node_color="salmon", font_size=10, font_weight="bold")
    plt.title("Graph with edges only")
    plt.show()

