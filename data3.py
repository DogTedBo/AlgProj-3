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

