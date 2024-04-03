
#ingnore this code, for testing purposes only
import networkx as nx
import matplotlib.pyplot as plt

# Original graph edge list
edges1 = [(4, 12), (4, 1), (4, 2), (1, 3), (3, 2), (3, 5), (5, 6), (6, 8), (8, 9), (9, 11), 
         (11, 12), (6, 7), (7, 10), (10, 11), (2, 1), (10, 9), (10, 9), (9, 5)]

# Strongly connected components
components = [{12}, {11}, {5, 6, 7, 8, 9, 10}, {1, 2, 3}, {4}]

# Create a directed graph for the DAG
dag = nx.DiGraph()

# Add nodes for each strongly connected component
for component in components:
    dag.add_node(tuple(component))

# Add edges between nodes based on edges between components in the original graph
for edge in edges1:
    u, v = edge
    for i, component_i in enumerate(components):
        if u in component_i:
            for j, component_j in enumerate(components):
                if v in component_j and i != j:
                    dag.add_edge(tuple(component_i), tuple(component_j))

# Draw the DAG
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(dag)
nx.draw_networkx_nodes(dag, pos, node_size=1500, node_color="lightblue")
nx.draw_networkx_edges(dag, pos, arrows=True)
nx.draw_networkx_labels(dag, pos, font_size=10, font_weight="bold")
plt.title("DAG of Strongly Connected Components")
plt.show()
