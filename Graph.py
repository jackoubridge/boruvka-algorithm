class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.edges = []

    def add_edge(self, source, destination, weight):
        self.edges.append([source, destination, weight])
        print("Added edge of weight %s between node %s and node %s" % (weight, source, destination))

    def find_component(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find_component(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, i, j):
        i_parent = self.find_component(parent, i)
        j_parent = self.find_component(parent, j)

        if rank[i_parent] < rank[j_parent]:
            parent[i_parent] = j_parent
        elif rank[i_parent] > rank[j_parent]:
            parent[j_parent] = i_parent
        else:
            parent[j_parent] = i_parent
            rank[i_parent] += 1

    def mst(self):
        parent = [i for i in range(self.num_nodes)]
        rank = [0] * self.num_nodes
        total_weight = 0
        num_trees = self.num_nodes

        self.edges.sort(key=lambda x: x[2])

        for u, v, w in self.edges:
            set1 = self.find_component(parent, u)
            set2 = self.find_component(parent, v)

            if set1 != set2:
                total_weight += w
                self.union(parent, rank, set1, set2)
                num_trees -= 1

            if num_trees == 1:
                break

        return total_weight
