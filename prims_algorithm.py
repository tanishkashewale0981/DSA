class Graph:
    def __init__(self):
        self.v = 0
        self.e = 0
        self.G = []

    def create(self):
        self.v = int(input("Enter NO of vertices: "))
        self.e = int(input("Enter No of Edges: "))
        self.G = [[0 for i in range(self.v)]
                  for j in range(self.v)]

        for i in range(self.e):
            print(f"\nEnter Edge {i + 1}")
            u = int(input("Enter the start vertex: "))
            v = int(input("Enter End Vertex: "))
            w = int(input("Enter weight: "))
            self.G[u][v] = self.G[v][u] = w

    def display(self):
        for i in range(self.v):
            for j in range(self.v):
                print(self.G[i][j], end=" ")
            print()

    def prims(self):
        selected = [False] * self.v
        key = [float('inf')] * self.v
        parent = [-1] * self.v
        key[0] = 0

        for i in range(self.v):
            min_weight = float('inf')
            u = -1

            for j in range(self.v):
                if not selected[j] and key[j] < min_weight:
                    min_weight = key[j]
                    u = j

            if u == -1:
                print("Graph is disconnected!")
                return

            selected[u] = True

            for v in range(self.v):
                if (self.G[u][v] != 0
                        and not selected[v]
                        and self.G[u][v] < key[v]):
                    key[v] = self.G[u][v]
                    parent[v] = u

        total = 0
        print("\nEdges in Minimum Spanning Tree:")

        for i in range(1, self.v):
            print(parent[i], "-", i, ":", self.G[i][parent[i]])
            total += self.G[i][parent[i]]

        print("Total weight of MST:", total)


ob = Graph()
ob.create()
ob.display()
ob.prims()