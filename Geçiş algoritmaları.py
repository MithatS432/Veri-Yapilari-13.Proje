from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    print("BFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# Aynı grafı kullanıyoruz
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

bfs(graph, 'A')




def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    print(start, end=" ")
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

print("\nDFS Traversal:", end=" ")
dfs(graph, 'A')
