
#Q2 - find the strongly connected components of a directed graph
import networkx as nx
from data3 import edges1

# function to find the strongly connected components of a directed graph
def find_strongly_connected_components(edges1):
    G = nx.DiGraph(edges1)
    return list(nx.strongly_connected_components(G)) # return the strongly connected components as a list

# define the edges of the directed graph

scc = find_strongly_connected_components(edges1)
print(scc)
