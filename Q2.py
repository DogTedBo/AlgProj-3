
#Q2 - find the strongly connected components of a directed graph
import networkx as nx
import matplotlib.pyplot as plt
from data3 import edges1

# function to find the strongly connected components of a directed graph
def find_strongly_connected_components(edges1):
    G = nx.DiGraph(edges1)
    return list(nx.strongly_connected_components(G)) # return the strongly connected components as a list
    
    


def graph2(edges1):
    G = nx.DiGraph(edges1)
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color="lightgreen", font_size=10, font_weight="bold")
    plt.title("Directed Graph")
    plt.show()


    
    
    




