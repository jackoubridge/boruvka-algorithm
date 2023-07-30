from Graph import Graph


def main():
    
    # Initialise the graph and add its weighted edges
    graph = Graph(6)
    graph.add_edge(0, 1, 1)
    graph.add_edge(0, 3, 4)
    graph.add_edge(1, 3, 7)
    graph.add_edge(1, 4, 3)
    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 5, 6)
    graph.add_edge(3, 4, 8)
    graph.add_edge(4, 5, 2)
    graph.add_edge(5, 2, 9)

    # Find MST
    print("Minimum spanning tree weight is %s" % graph.mst())


if __name__ == "__main__":
    main()
