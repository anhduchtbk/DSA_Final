INF = float('inf')

def bellman_ford(graph, src, dst):
    # Khởi tạo khoảng cách từ đỉnh bắt đầu đến các đỉnh khác là vô cực
    distance = {node: float('inf') for node in graph}
    distance[src] = 0
    path = dict()

    # Thực hiện thuật toán Bellman-Ford
    for i in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                if distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]
                    path[u] = v

    # Kiểm tra nếu có chu trình âm trong đồ thị
    for u in graph:
        for v in graph[u]:
            assert distance[v] <= distance[u] + graph[u][v], "Đồ thị có chu trình âm"


    result = [src]
    for m, n in path.items():
        result.append(n)
    # Trả về khoảng cách từ đỉnh bắt đầu đến đỉnh kết thúc
    return distance[dst], result

graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'D': 3, 'E': 6},
    'C': {'B': 2, 'D': 4},
    'D': {'E': 2},
    'E': {},
    'F': {'C': 1}
}

start = 'A'
print(bellman_ford(graph, start, 'E'))