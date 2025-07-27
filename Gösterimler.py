# Düğüm kümesi: A, B, C
# Kenarlar: A-B, A-C, B-C

nodes = ['A', 'B', 'C']
adj_matrix = [
    [0, 1, 1],  # A -> B, C
    [1, 0, 1],  # B -> A, C
    [1, 1, 0]   # C -> A, B
]

print("Komşuluk Matrisi:")
for row in adj_matrix:
    print(row)




graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

print("\nKomşuluk Listesi:")
for node, neighbors in graph.items():
    print(f"{node}: {neighbors}")
