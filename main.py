import numpy as np
import math

def main():
    
    # Generate random graph with x nodes
    graph = generate_graph(10)

    graph = [[4, 2, 3, 1, 5],
             [6, 4, 5, 2, 1]]

    visited_nodes = []

    # For each node in the graph, find its cheapest neighbour
    for node in graph:
        print(node.index(min(node)))

    print(math.inf)

def generate_graph(num_nodes):
    return

if __name__ == '__main__':
    main()

