import random
import networkx as nx

def graph(node1, egde1):
# Sinh số đỉnh và cạnh ngẫu nhiên
    num_nodes = random.randint(node1, egde1)
    num_edges = random.randint(num_nodes - 1, num_nodes * (num_nodes - 1) // 2)

    # Tạo đồ thị ngẫu nhiên
    G = nx.gnm_random_graph(num_nodes, num_edges)

    # Gán trọng số ngẫu nhiên cho các cạnh
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(1, 10)

    # Chuyển đổi đồ thị thành dạng dict như mẫu
    graph = {}
    for u in G.nodes():
        neighbors = {}
        for v in G.neighbors(u):
            neighbors[str(v)] = G[u][v]['weight']
        graph[str(u)] = neighbors

    print(graph)
    return graph