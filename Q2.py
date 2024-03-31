
#Q2 - find the strongly connected components of a directed graph
import networkx as nx

# function to find the strongly connected components of a directed graph
def find_strongly_connected_components(edges):
    G = nx.DiGraph(edges)
    return list(nx.strongly_connected_components(G)) # return the strongly connected components as a list

# define the edges of the directed graph
edges = [
    (1, 2), (1, 3), (2, 4), (3, 4), (4, 3), (4, 5), (5, 6), (5, 11),
    (6, 7), (7, 8), (8, 9), (9, 6), (9, 10), (11, 12), (12, 10), (10, 5)
]

scc = find_strongly_connected_components(edges)
print(scc)
