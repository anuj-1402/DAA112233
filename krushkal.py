class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
    
    def find(self, item):
        if self.parent[item] == item:
            return item
        self.parent[item] = self.find(self.parent[item])  # Path compression
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            self.parent[root2] = root1


def kruskal_mst(vertices, edges):
    ds = DisjointSet(vertices)
    mst = []
    total_cost = 0

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost


# Example usage
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('C', 'D', 1),
    ('D', 'E', 2),
    ('C', 'E', 5)
]

mst, cost = kruskal_mst(vertices, edges)

print("Minimum Spanning Tree (MST):")
for u, v, weight in mst:
    print(f"{u} - {v}: {weight}")
print(f"Total cost of MST: {cost}")
