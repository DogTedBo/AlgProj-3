from data3 import edges
from dijkstra import dijkstra
from prim import prim
from Q3 import visualize_graph
import networkx as nx
from matplotlib import pyplot as plt

def task1():
    # Task 1: Representing an Undirected Graph and Answering Questions Computationally
    print("\nTask 1: Representing an Undirected Graph and Answering Questions")
    # Implement Task 1 here...

def task2():
    # Task 2: Decomposing a Connected Digraph into Strongly Connected Components
    print("\nTask 2: Decomposing a Connected Digraph into Strongly Connected Components")
    # Implement Task 2 here...

def task3():
    # Task 3: Applying Dijkstra's Algorithm and Minimum Spanning Tree Algorithm
    print("\nTask 3: Applying Dijkstra's Algorithm and Minimum Spanning Tree Algorithm")
    visualize_graph()
    

def main():
    while True:
        print("\nSelect a task to perform:")
        print("1. Task 1: Representing an Undirected Graph")
        print("2. Task 2: Decomposing a Connected Digraph into Strongly Connected Components")
        print("3. Task 3: Applying Dijkstra's Algorithm and Minimum Spanning Tree Algorithm")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            task3()
            
            
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()