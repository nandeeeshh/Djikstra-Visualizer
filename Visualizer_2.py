import sys
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0
    visited = set()

    shortest_path = {}

    while len(visited) < len(graph):
        min_distance = sys.maxsize
        min_node = None

        for node in graph:
            if distances[node] < min_distance and node not in visited:
                min_distance = distances[node]
                min_node = node

        visited.add(min_node)

        for neighbor, weight in graph[min_node].items():
            distance = distances[min_node] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = min_node

    return distances, shortest_path

def get_shortest_path(end, shortest_path):
    path = []
    node = end

    while node is not None:
        path.append(node)
        node = shortest_path.get(node)

    path.reverse()
    return path

def visualize_graph(graph, shortest_path, shortest_path_to_end):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(graph)

    nx.draw_networkx_nodes(graph, pos, node_color='lightblue', node_size=500)

    nx.draw_networkx_edges(graph, pos, width=1, alpha=0.5)

    path_edges = [(shortest_path[i], i) for i in shortest_path.keys()]
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, width=3, edge_color='red')

    path_edges = [(shortest_path_to_end[i], i) for i in shortest_path_to_end.keys()]
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, width=3, edge_color='green')

    nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')

    plt.axis('off')
    plt.show()

def make_dict(s):
    d={}
    for i in range (0,len(s)-1):
        d[s[i]]=s[i+1]
    return d

# Example usage
import networkx as nx

graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 1, 'D': 2},
    'C': {'A': 3, 'B': 1, 'D': 4, 'E': 8},
    'D': {'B': 2, 'C': 4, 'E': 6, 'F': 3},
    'E': {'C': 8, 'D': 6},
    'F': {'D': 3}
}

start_node = 'A'
end_node = 'E'

distances, shortest_path = dijkstra(graph, start_node)
print(shortest_path)
shortest_path_to_end = get_shortest_path(end_node, shortest_path)
print(shortest_path_to_end)
shortest_path_to_end = make_dict(shortest_path_to_end)
print(shortest_path_to_end)

nx_graph = nx.Graph(graph)

visualize_graph(nx_graph, shortest_path, shortest_path_to_end)


